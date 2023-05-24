from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Получение рандомного вопроса'
    secret: str = 'SECRET'
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    @property
    def database_url(self) -> str:
        """Получить ссылку для подключения к DB."""
        return (
            "postgresql://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()