from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str

    debug: bool

    secret_key: str
        
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str
    aws_s3_bucket: str 

    # JWT
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Database
    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


settings = Settings()
