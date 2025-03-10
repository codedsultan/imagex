from .mockup_service_interface import MockupServiceInterface
import cv2
import numpy as np
import base64

class OpenCVMockupService(MockupServiceInterface):
    def process_mockup(self, payload: dict) -> dict:
        image_path = payload.get("image_path", "default.png")
        position = payload.get("position", "front")
        color = payload.get("color_code", "#FFFFFF")
        
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if img is None:
            hex_color = color.lstrip("#")
            if len(hex_color) == 6:
                r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            else:
                r, g, b = (255, 255, 255)
            bgr_color = (b, g, r)
            img = np.zeros((600, 800, 3), dtype=np.uint8)
            img[:] = bgr_color
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f"Position: {position}", (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        ret, buffer = cv2.imencode('.png', img)
        if not ret:
            raise Exception("Failed to encode image using OpenCV.")
        img_str = base64.b64encode(buffer).decode("utf-8")
        return {
            "preview_url": f"data:image/png;base64,{img_str}",
            "message": "Image processed successfully using OpenCV."
        }
