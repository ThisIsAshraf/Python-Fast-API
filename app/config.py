from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database Configuration
    
    DATABASE_HOST_NAME: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    
    # Authentication Settings
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()