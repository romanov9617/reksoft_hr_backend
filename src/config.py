from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DB_PROD_HOST: str
    DB_PROD_PORT: int
    DB_PROD_USER: str
    DB_PROD_PASSWORD: str
    DB_PROD_NAME: str

    @property
    def DB_PROD_URL(self):
        return f"postgresql+asyncpg://{self.DB_PROD_USER}:{self.DB_PROD_PASSWORD}@{self.DB_PROD_HOST}:{self.DB_PROD_PORT}/{self.DB_PROD_NAME}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()