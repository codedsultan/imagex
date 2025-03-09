from app.core.config import settings
from app.services.mockup_service_interface import MockupServiceInterface

def get_storage_service():
    if settings.STORAGE_TYPE.lower() == "s3":
        from app.services.s3_storage_service import S3StorageService
        return S3StorageService(bucket_name=settings.BUCKET_NAME)
    else:
        from app.services.local_storage_service import LocalStorageService
        return LocalStorageService(storage_path=settings.LOCAL_STORAGE_PATH)

def get_mockup_service() -> MockupServiceInterface:
    if settings.MOCKUP_SERVICE_TYPE.lower() == "opencv":
        from app.services.opencv_mockup_service import OpenCVMockupService
        return OpenCVMockupService()
    else:
        from app.services.pillow_mockup_service import PillowMockupService
        return PillowMockupService()
