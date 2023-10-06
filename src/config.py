from pydantic import BaseConfig
from dotenv import dotenv_values

config = dotenv_values("../.env")


class Settings:
    host: str = config.get("HOST")
    port: int = int(config.get("PORT"))


settings = Settings()

