import os
import uuid
from app.services.storage_service_interface import StorageServiceInterface

class LocalStorageService(StorageServiceInterface):
    def __init__(self, storage_path: str = "storage"):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    def store_image(self, image_data: bytes, filename: str = None) -> str:
        if not filename:
            filename = f"{uuid.uuid4()}.png"
        file_path = os.path.join(self.storage_path, filename)
        with open(file_path, "wb") as f:
            f.write(image_data)
        return filename

    def get_image_url(self, filename: str) -> str:
        return f"/static/{filename}"
