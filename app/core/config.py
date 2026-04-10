from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    base_domain: str = "example.com"  # for subdomain tenancy
    tenant_header: str = "X-Tenant-ID"

    class Config:
        env_file = ".env"

settings = Settings()
