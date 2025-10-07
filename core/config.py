from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Force load .env
load_dotenv()
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))


class Settings(BaseSettings):
    # Database Config
    db_username: str
    db_password: str
    db_hostname: str
    db_port: str
    db_name: str

    # JWT Config
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30  # in minutes

    class Config:
        env_file = ".env"
        case_sensitive = False


print("DB_USERNAME:", os.getenv("db_username"))
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
print("ENV exists?", env_path.exists())  # Should print True
load_dotenv(dotenv_path=env_path)

print("DB_USERNAME:", os.getenv("db_username"))  # Should print postgres



settings = Settings()