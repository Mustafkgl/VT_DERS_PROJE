import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Uygulama yapılandırma sınıfı"""

    # Secret key for JWT
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

    # Database configuration
    DB_USER = os.getenv('DB_USER', 'library_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'library123')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')