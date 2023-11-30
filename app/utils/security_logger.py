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