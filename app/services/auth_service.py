import jwt
import logging
from datetime import datetime, timedelta
from config import Config
from app.repositories.user_repository import UserRepository
from app.utils.validators import InputValidator, PasswordValidator
from app.utils.security_logger import security_logger

# Logger
logger = logging.getLogger(__name__)

class AuthService:
    """Kimlik Doğrulama İş Mantığı"""

    @staticmethod
    def register(username: str, email: str, password: str, role: str = 'member') -> dict:
        """Kullanıcı kaydı"""
        logger.info(f'Registration attempt for username: {username}')

        # Input validation
        if not username or not email or not password:
            logger.warning(f'Registration failed: Missing fields for {username}')
            return {'success': False, 'message': 'Tüm alanlar gerekli'}

        # Kullanıcı adı kontrolü
        if not InputValidator.validate_username(username):
            security_logger.log_validation_error('username', username, 'Invalid format')
            return {'success': False, 'message': 'Geçersiz kullanıcı adı (3-50 karakter, sadece harf, rakam, _ ve -)'}

        # Email kontrolü
        if not InputValidator.validate_email(email):
            security_logger.log_validation_error('email', email, 'Invalid format')
            return {'success': False, 'message': 'Geçersiz email formatı'}

        # Şifre kontrolü (güçlendirilmiş)