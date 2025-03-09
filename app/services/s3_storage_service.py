import uuid
import boto3
from botocore.exceptions import ClientError
from app.services.storage_service_interface import StorageServiceInterface
from app.core.config import settings

class S3StorageService(StorageServiceInterface):
    def __init__(self, bucket_name: str, region: str = "us-east-1"):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            "s3",
            endpoint_url=settings.S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=region,
        )

    def store_image(self, image_data: bytes, filename: str = None) -> str:
        if not filename:
            filename = f"{uuid.uuid4()}.png"
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=filename,
                Body=image_data,
                ContentType="image/png"
            )
        except ClientError as e:
            raise Exception(f"Failed to store image in S3: {e}")
        return filename

    def get_image_url(self, filename: str) -> str:
        try:
            url = self.s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": self.bucket_name, "Key": filename},
                ExpiresIn=3600
            )
        except ClientError as e:
            raise Exception(f"Failed to generate URL: {e}")
        return url
