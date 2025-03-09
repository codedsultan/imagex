import pytest
from app.services.pillow_mockup_service import PillowMockupService
from app.services.opencv_mockup_service import OpenCVMockupService

@pytest.fixture
def sample_payload():
    return {
        "image_path": "nonexistent.png",
        "position": "front",
        "color_code": "#FF0000",
        "render_settings": {"scale": 1, "x_offset": 0, "y_offset": 0, "rotation": 0}
    }

def test_pillow_mockup_service(sample_payload):
    service = PillowMockupService()
    result = service.process_mockup(sample_payload)
    assert "preview_url" in result
    assert "Pillow" in result["message"]

def test_opencv_mockup_service(sample_payload):
    service = OpenCVMockupService()
    result = service.process_mockup(sample_payload)
    assert "preview_url" in result
    assert "OpenCV" in result["message"]
