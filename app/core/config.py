import os
from typing import List

class Settings:
    PROJECT_NAME: str = "CrunchyCraft Cinematic Experience API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Database: Default to local SQLite for immediate zero-config operation,
    # or override with DATABASE_URL for PostgreSQL/Supabase
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite:///./crunchycraft_cinematic.db"
    )
    
    # JWT / Auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "crunchycraft_super_secret_concept_key_2026_crunch")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Supabase configuration (optional)
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY", "")
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://haldiram-cinematic.vercel.app",
        "*"
    ]

settings = Settings()
