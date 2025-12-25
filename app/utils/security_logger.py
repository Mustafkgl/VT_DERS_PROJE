"""
Güvenlik Event Logging
Tüm güvenlik olaylarını detaylı şekilde logla
"""

import logging
import json
import os
from datetime import datetime
from flask import request, has_request_context


class SecurityLogger:
    """Güvenlik olayları için özel logger"""

    def __init__(self):
        self.logger = logging.getLogger('security')
        self.logger.setLevel(logging.INFO)

        # Security log file handler
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        handler = logging.handlers.RotatingFileHandler(
            os.path.join(log_dir, 'security.log'),
            maxBytes=10485760,  # 10MB
            backupCount=20  # Güvenlik logları daha fazla tutulur
        )

        # JSON formatter
        from app.utils.logger import JSONFormatter
        handler.setFormatter(JSONFormatter())
        self.logger.addHandler(handler)

    def _get_request_info(self):
        """Request bilgilerini al"""
        if has_request_context():
            return {
                'ip': request.remote_addr,
                'user_agent': request.headers.get('User-Agent', 'Unknown'),
                'method': request.method,
                'path': request.path,
                'referrer': request.referrer
            }
        return {}

    def log_login_attempt(self, username, success, user_id=None, reason=None):
        """
        Login denemesi logla

        Args:
            username: Kullanıcı adı
            success: Başarılı mı
            user_id: Kullanıcı ID (başarılıysa)
            reason: Başarısız olma nedeni
        """
        extra_data = {
            'event': 'login_attempt',
            'username': username,
            'success': success,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        if success:
            extra_data['user_id'] = user_id
            self.logger.info(
                f'Successful login: {username}',
                extra={'extra_data': extra_data}
            )
        else:
            extra_data['reason'] = reason
            self.logger.warning(
                f'Failed login attempt: {username} - {reason}',
                extra={'extra_data': extra_data}
            )

    def log_logout(self, user_id, username):
        """Logout logla"""
        extra_data = {
            'event': 'logout',
            'user_id': user_id,
            'username': username,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        self.logger.info(
            f'User logout: {username}',
            extra={'extra_data': extra_data}
        )

    def log_registration(self, username, email, role, success):
        """Kayıt işlemini logla"""
        extra_data = {
            'event': 'user_registration',
            'username': username,
            'email': email,
            'role': role,
            'success': success,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        self.logger.info(
            f'User registration: {username} ({role})',
            extra={'extra_data': extra_data}
        )

    def log_unauthorized_access(self, endpoint, user_id=None, required_role=None):
        """Yetkisiz erişim denemesi logla"""
        extra_data = {
            'event': 'unauthorized_access',
            'endpoint': endpoint,
            'user_id': user_id,
            'required_role': required_role,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        self.logger.warning(
            f'Unauthorized access attempt to {endpoint}',
            extra={'extra_data': extra_data}
        )

    def log_token_validation(self, success, reason=None, user_id=None):
        """Token validasyon logla"""
        extra_data = {
            'event': 'token_validation',
            'success': success,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        if success:
            extra_data['user_id'] = user_id
            self.logger.debug(
                'Token validation successful',
                extra={'extra_data': extra_data}
            )
        else:
            extra_data['reason'] = reason
            self.logger.warning(
                f'Token validation failed: {reason}',
                extra={'extra_data': extra_data}
            )

    def log_password_change(self, user_id, username, success):
        """Şifre değişikliği logla"""
        extra_data = {
            'event': 'password_change',
            'user_id': user_id,
            'username': username,
            'success': success,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        self.logger.info(
            f'Password change for user {username}',
            extra={'extra_data': extra_data}
        )

    def log_suspicious_activity(self, activity_type, details):
        """
        Şüpheli aktivite logla

        Args:
            activity_type: SQL Injection, XSS, Brute Force, etc.
            details: Aktivite detayları
        """
        extra_data = {
            'event': 'suspicious_activity',
            'activity_type': activity_type,
            'details': details,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        self.logger.critical(
            f'SUSPICIOUS ACTIVITY: {activity_type}',
            extra={'extra_data': extra_data}
        )

    def log_data_access(self, user_id, resource_type, resource_id, action):
        """
        Veri erişimi logla (Audit Trail)

        Args:
            user_id: Kullanıcı ID
            resource_type: book, borrowing, fine, etc.
            resource_id: Kaynak ID
            action: read, create, update, delete
        """
        extra_data = {
            'event': 'data_access',
            'user_id': user_id,
            'resource_type': resource_type,
            'resource_id': resource_id,
            'action': action,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        self.logger.info(
            f'Data access: {action} {resource_type}#{resource_id} by user#{user_id}',
            extra={'extra_data': extra_data}
        )

    def log_validation_error(self, field, value, error_type):
        """
        Validation hatası logla

        Args:
            field: Alan adı
            value: Hatalı değer
            error_type: Hata tipi (XSS, SQL Injection attempt, etc.)
        """
        extra_data = {
            'event': 'validation_error',
            'field': field,
            'value': value[:100] if len(str(value)) > 100 else value,  # Truncate
            'error_type': error_type,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        self.logger.warning(
            f'Validation error: {error_type} in {field}',
            extra={'extra_data': extra_data}
        )

    def log_rate_limit_exceeded(self, user_id=None, endpoint=None):
        """Rate limit aşımı logla"""
        extra_data = {
            'event': 'rate_limit_exceeded',
            'user_id': user_id,
            'endpoint': endpoint,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        self.logger.warning(
            f'Rate limit exceeded for {endpoint or "unknown endpoint"}',
            extra={'extra_data': extra_data}
        )

    def log_admin_action(self, admin_id, action, target_type, target_id, details=None):
        """
        Admin işlemlerini logla

        Args:
            admin_id: Admin kullanıcı ID
            action: create_book, delete_user, etc.
            target_type: book, user, etc.
            target_id: Hedef ID
            details: Ek detaylar
        """
        extra_data = {
            'event': 'admin_action',
            'admin_id': admin_id,
            'action': action,
            'target_type': target_type,
            'target_id': target_id,
            'timestamp': datetime.utcnow().isoformat(),
            **self._get_request_info()
        }

        if details:
            extra_data['details'] = details

        self.logger.info(
            f'Admin action: {action} on {target_type}#{target_id} by admin#{admin_id}',
            extra={'extra_data': extra_data}
        )


# Singleton instance
security_logger = SecurityLogger()


# Logging importları
import logging.handlers
