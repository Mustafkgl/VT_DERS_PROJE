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
    DB_NAME = os.getenv('DB_NAME', 'library_db')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Configuration
    JWT_ALGORITHM = 'HS256'
    JWT_EXPIRATION_HOURS = 24

    # CORS Configuration
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:5000').split(',')  # Comma-separated list

    # Environment
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FORCE_HTTPS = os.getenv('FORCE_HTTPS', 'False').lower() == 'true'
