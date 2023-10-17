from pydantic import BaseConfig
from dotenv import dotenv_values

config = dotenv_values("../.env")


class Settings:
    host: str = config.get("HOST")
    port: int = int(config.get("PORT"))
    SECRET_KEY: str = config.get("SECRET_KEY")
    ALGORITHM: str = config.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(config.get("ACCESS_TOKEN_EXPIRE_MINUTES"))


settings = Settings()
