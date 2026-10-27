from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    blizzard_client_id: str
    blizzard_client_secret: str
    database_url: str
    connected_realm_id: int = 3391
    region: str = "eu"


settings = Settings() # pyright: ignore[reportCallIssue]
