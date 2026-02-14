from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  DEBUG: bool
  DATABASE_URL: str

  CLOUDINARY_CLOUD_NAME: str
  CLOUDINARY_API_KEY: str
  CLOUDINARY_API_SECRET: str

  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    case_sensitive=False,
    extra="ignore"  
  )

settings = Settings()
