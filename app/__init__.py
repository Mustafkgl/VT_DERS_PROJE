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

    # Security Headers ekle
    from app.utils.security_headers import add_security_headers
    add_security_headers(app)

    # Logging sistemini başlat
    from app.utils.logger import setup_logging
    setup_logging(app)

    # Error handler'ları kaydet
    from app.utils.error_handlers import register_error_handlers
    register_error_handlers(app)

    # Blueprint'leri kaydet
    from app.controllers.auth_controller import auth_bp
    from app.controllers.book_controller import book_bp
    from app.controllers.borrowing_controller import borrowing_bp
    from app.controllers.fine_controller import fine_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(borrowing_bp)
    app.register_blueprint(fine_bp)

    # Ana sayfa route'ları
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/register')
    def register_page():
        return render_template('register.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    return app
