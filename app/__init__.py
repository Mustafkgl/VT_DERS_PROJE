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