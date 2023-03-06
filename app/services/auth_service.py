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
        is_valid, error_message = PasswordValidator.validate_password(password)
        if not is_valid:
            logger.warning(f'Registration failed: {error_message} for {username}')
            return {'success': False, 'message': error_message}

        # Rol kontrolü
        if role not in ['admin', 'member']:
            logger.warning(f'Registration failed: Invalid role {role} for {username}')
            return {'success': False, 'message': 'Geçersiz rol'}

        # Girdi temizleme
        username = InputValidator.sanitize_text(username, max_length=80)
        email = InputValidator.sanitize_text(email, max_length=120)

        # Kullanıcı adı ve email kontrolü
        if UserRepository.find_by_username(username):
            logger.warning(f'Registration failed: Username {username} already exists')
            return {'success': False, 'message': 'Kullanıcı adı zaten kullanımda'}

        if UserRepository.find_by_email(email):
            logger.warning(f'Registration failed: Email {email} already registered')
            return {'success': False, 'message': 'Email zaten kayıtlı'}

        # Kullanıcı oluştur
        user = UserRepository.create(username, email, password, role)
        if user:
            # Başarılı kayıt
            security_logger.log_registration(username, email, role, True)
            logger.info(f'User registered successfully: {username} (ID: {user.id})')
            return {'success': True, 'message': 'Kayıt başarılı', 'user': user.to_dict()}

        # Kayıt başarısız
        security_logger.log_registration(username, email, role, False)
        logger.error(f'Registration failed: Database error for {username}')
        return {'success': False, 'message': 'Kayıt başarısız'}

    @staticmethod
    def login(username: str, password: str) -> dict:
        """Kullanıcı girişi"""
        logger.info(f'Login attempt for username: {username}')

        user = UserRepository.find_by_username(username)

        if not user or not user.check_password(password):
            # Başarısız login
            reason = 'User not found' if not user else 'Invalid password'
            security_logger.log_login_attempt(username, False, reason=reason)
            logger.warning(f'Failed login attempt for {username}: {reason}')
            return {'success': False, 'message': 'Kullanıcı adı veya şifre hatalı'}

        # JWT token oluştur
        token = AuthService.generate_token(user)

        # Başarılı login
        security_logger.log_login_attempt(username, True, user_id=user.id)
        logger.info(f'Successful login: {username} (ID: {user.id}, Role: {user.role})')

        return {
            'success': True,
            'message': 'Giriş başarılı',
            'token': token,
            'user': user.to_dict()
        }

    @staticmethod
    def generate_token(user):
        """JWT token oluştur"""
        payload = {
            'user_id': user.id,
            'username': user.username,
            'role': user.role,
            'exp': datetime.utcnow() + timedelta(hours=Config.JWT_EXPIRATION_HOURS)
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
        return token

    @staticmethod
    def verify_token(token: str) -> dict:
        """JWT token doğrula"""
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
            # Başarılı validasyon
            security_logger.log_token_validation(True, user_id=payload.get('user_id'))
            return {'success': True, 'payload': payload}
        except jwt.ExpiredSignatureError:
            # Token süresi dolmuş
            security_logger.log_token_validation(False, reason='Token expired')
            logger.warning('Token validation failed: Expired token')
            return {'success': False, 'message': 'Token süresi dolmuş'}
        except jwt.InvalidTokenError as e:
            # Geçersiz token
            security_logger.log_token_validation(False, reason='Invalid token')
            logger.warning(f'Token validation failed: Invalid token - {str(e)}')
            return {'success': False, 'message': 'Geçersiz token'}

    @staticmethod
    def get_current_user(token):
        """Token'dan kullanıcı bilgisi al"""
        result = AuthService.verify_token(token)
        if result['success']:
            user_id = result['payload']['user_id']
            user = UserRepository.find_by_id(user_id)
            if user:
                return {'success': True, 'user': user}
        return {'success': False, 'message': 'Kullanıcı bulunamadı'}
