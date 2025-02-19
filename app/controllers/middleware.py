from functools import wraps
from flask import request, jsonify
from app.services.auth_service import AuthService
from app.utils.security_logger import security_logger
import logging

logger = logging.getLogger(__name__)

def token_required(f):
    """Token zorunlu middleware"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Header'dan token al
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]  # "Bearer <token>"
            except IndexError:
                return jsonify({'success': False, 'message': 'Geçersiz token formatı'}), 401

        if not token:
            return jsonify({'success': False, 'message': 'Token gerekli'}), 401

        # Token doğrula
        result = AuthService.verify_token(token)
        if not result['success']:
            return jsonify(result), 401

        return f(result['payload'], *args, **kwargs)

    return decorated

def admin_required(f):
    """Admin yetkisi zorunlu middleware"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Header'dan token al