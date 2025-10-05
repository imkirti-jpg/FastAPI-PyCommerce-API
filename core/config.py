from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Force load .env
load_dotenv()


class Settings(BaseSettings):
    # Database Config
    db_username: str
    db_password: str
    db_hostname: str
    db_port: str
    db_name: str

    # JWT Config
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
        case_sensitive = False


print("DB_USERNAME:", os.getenv("db_username"))



settings = Settings()