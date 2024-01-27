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

