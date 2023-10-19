from flask import Flask, render_template
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from app.models import db

migrate = Migrate()
limiter = None  # Global limiter instance

def create_app():
    """Flask uygulaması oluştur"""
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    # CORS Configuration
    CORS(app, resources={
        r"/api/*": {
            "origins": app.config.get('CORS_ORIGINS', ["http://localhost:5000"]),
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "expose_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True,
            "max_age": 3600
        }
    })

    # Veritabanı başlat
    db.init_app(app)

    # Migration başlat
    migrate.init_app(app, db)

    # Rate Limiting başlat
    global limiter
    from app.utils.rate_limiter import get_limiter
    limiter = get_limiter()
    limiter.init_app(app)
