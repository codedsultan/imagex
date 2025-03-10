from .mockup_service_interface import MockupServiceInterface
from PIL import Image, ImageDraw
import io
import base64

class PillowMockupService(MockupServiceInterface):
    def process_mockup(self, payload: dict) -> dict:
        image_path = payload.get("image_path", "default.png")
        position = payload.get("position", "front")
        color = payload.get("color_code", "#FFFFFF")
        render_settings = payload.get("render_settings", {"scale": 1, "x_offset": 0, "y_offset": 0, "rotation": 0})
        
        try:
            img = Image.open(image_path).convert("RGBA")
        except Exception:
            img = Image.new("RGBA", (800, 600), color)
        
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), f"Position: {position}", fill="black")
        
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return {
            "preview_url": f"data:image/png;base64,{img_str}",
            "message": "Image processed successfully using Pillow."
        }
