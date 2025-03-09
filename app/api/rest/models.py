from pydantic import BaseModel, Field
from typing import Any, Dict

class ProcessImageRequest(BaseModel):
    image_path: str = Field(..., description="Path to the input image")
    position: str = Field(..., description="Desired position (e.g. front, back, center, breast_region)")
    color_code: str = Field("#FFFFFF", description="Hex color code")
    render_settings: Dict[str, Any] = Field(
        default_factory=lambda: {"scale": 1, "x_offset": 0, "y_offset": 0, "rotation": 0},
        description="Render settings for scaling, offsets, and rotation"
    )

class ProcessImageResponse(BaseModel):
    preview_url: str = Field(..., description="URL or base64 encoded image of the preview")
    message: str = Field(..., description="Status message")
