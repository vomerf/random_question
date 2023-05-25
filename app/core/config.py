from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Получение рандомного вопроса'
    secret: str = 'SECRET'
    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: str
    url = 'https://jservice.io/api/random'
    @property
    def database_url(self) -> str:
        """Получить ссылку для подключения к DB."""
        return (
            "postgresql://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.db_host}:{self.db_port}/{self.postgres_db}"
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()