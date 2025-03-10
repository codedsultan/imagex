from abc import ABC, abstractmethod
from typing import Optional

class StorageServiceInterface(ABC):
    @abstractmethod
    def store_image(self, image_data: bytes, filename: Optional[str] = None) -> str:
        """Store image data and return a reference (file name or key)."""
        pass

    @abstractmethod
    def get_image_url(self, filename: str) -> str:
        """Return a publicly accessible URL for the stored image."""
        pass
