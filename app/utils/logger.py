"""
Uygulama Logging Sistemi
Structured logging (JSON format) ile detaylı log tutma
"""

import logging
import json
import os
from datetime import datetime
from functools import wraps
from flask import request, has_request_context
import traceback


class JSONFormatter(logging.Formatter):
    """JSON formatında log mesajları"""

    def format(self, record):
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }

        # Request context varsa ekle
        if has_request_context():
            log_data['request'] = {
                'method': request.method,
                'path': request.path,
                'ip': request.remote_addr,
                'user_agent': request.headers.get('User-Agent', 'Unknown')
            }

        # Extra bilgiler varsa ekle
        if hasattr(record, 'extra_data'):
            log_data['extra'] = record.extra_data

        # Exception varsa ekle
        if record.exc_info:
            log_data['exception'] = {
                'type': record.exc_info[0].__name__,
                'message': str(record.exc_info[1]),
                'traceback': traceback.format_exception(*record.exc_info)
            }

        return json.dumps(log_data, ensure_ascii=False)


def setup_logging(app):
    """
    Logging yapılandırması

    Log dosyaları:
    - logs/app.log - Genel uygulama logları
    - logs/security.log - Güvenlik olayları
    - logs/error.log - Hatalar
    """

    # Log dizini oluştur
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Console handler (development)
    if app.debug:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        root_logger.addHandler(console_handler)

    # File handler - Genel loglar
    app_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_dir, 'app.log'),
        maxBytes=10485760,  # 10MB
        backupCount=10
    )
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(JSONFormatter())
    root_logger.addHandler(app_handler)

    # File handler - Error loglar
    error_handler = logging.handlers.RotatingFileHandler(
        os.path.join(log_dir, 'error.log'),
        maxBytes=10485760,  # 10MB
        backupCount=10
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(JSONFormatter())
    root_logger.addHandler(error_handler)

    # Flask app logger
    app.logger.info('Logging system initialized')

    return root_logger