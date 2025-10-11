from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from pathlib import Path


# Load .env first
env_path = Path('.') / '.env'
print("ENV exists?", env_path.exists())  # Should print True
load_dotenv(dotenv_path=env_path)

print("DB_USERNAME:", os.getenv("db_username"))  # Should now print postgres

class Settings(BaseSettings):
    # Database Config
    db_username: str
    db_password: str
    db_hostname: str
    db_port: str
    db_name: str
    database_url: str 

    # JWT Config
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30  # in minutes

    class Config:
        env_file = ".env"
        case_sensitive = False



settings = Settings()