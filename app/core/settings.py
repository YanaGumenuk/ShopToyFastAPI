from pydantic_settings import SettingsConfigDict, BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False
    )
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_URL: str

    @property
    def db_url(self) -> str:
        return self.DB_URL.format(
            db_user=self.DB_USER,
            db_pass=self.DB_PASS,
            db_host=self.DB_HOST,
            db_port=self.DB_PORT,
            db_name=self.DB_NAME,
        )

settings = Settings()

#    def get_url(self) -> str:
        #return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


