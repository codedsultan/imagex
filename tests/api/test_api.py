from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_image_endpoint():
    payload = {
        "image_path": "nonexistent.png",
        "position": "front",
        "color_code": "#00FF00",
        "render_settings": {"scale": 1, "x_offset": 0, "y_offset": 0, "rotation": 0}
    }
    response = client.post("/api/process-image", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "preview_url" in data
    assert "message" in data
