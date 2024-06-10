from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DB_PROD_HOST: str
    DB_PROD_PORT: int
    DB_PROD_USER: str
    DB_PROD_PASS: str
    DB_PROD_NAME: str

    FRONTEND_HOST: str
    FRONTEND_PORT: int

    @property
    def FRONTEND_URL(self):
        return f"http://{self.FRONTEND_HOST}:{self.FRONTEND_PORT}"

    @property
    def DB_PROD_URL(self):
        return f"postgresql+asyncpg://{self.DB_PROD_USER}:{self.DB_PROD_PASS}@{self.DB_PROD_HOST}:{self.DB_PROD_PORT}/{self.DB_PROD_NAME}"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
