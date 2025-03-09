from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Database Configuration
    DB_TYPE: str = Field(..., env="DB_TYPE")
    POSTGRES_URL: str = Field(..., env="POSTGRES_URL")
    MONGODB_URL: str = Field(..., env="MONGODB_URL")
    
    # Frontend URL
    FRONTEND_URL: str = Field("http://localhost:3000", env="FRONTEND_URL")
    
    # JWT Configuration
    JWT_SECRET: str = Field(..., env="JWT_SECRET")
    
    # Storage Configuration
    STORAGE_TYPE: str = Field("local", env="STORAGE_TYPE")  # "local" or "s3"
    LOCAL_STORAGE_PATH: str = Field("storage", env="LOCAL_STORAGE_PATH")
    S3_ENDPOINT_URL: str = Field(None, env="S3_ENDPOINT_URL")
    AWS_ACCESS_KEY_ID: str = Field(None, env="AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = Field(None, env="AWS_SECRET_ACCESS_KEY")
    BUCKET_NAME: str = Field(None, env="BUCKET_NAME")
    
    # Mockup Service Configuration
    MOCKUP_SERVICE_TYPE: str = Field("pillow", env="MOCKUP_SERVICE_TYPE")  # "pillow" or "opencv"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
