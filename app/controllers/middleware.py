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
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]
            except IndexError:
                logger.warning('Invalid token format in Authorization header')
                return jsonify({'success': False, 'message': 'Geçersiz token formatı'}), 401

        if not token:
            logger.warning(f'Missing token for admin endpoint: {request.path}')
            return jsonify({'success': False, 'message': 'Token gerekli'}), 401

        # Token doğrula
        result = AuthService.verify_token(token)
        if not result['success']:
            logger.warning(f'Invalid token for admin endpoint: {request.path}')
            return jsonify(result), 401

        # Admin kontrolü
        if result['payload']['role'] != 'admin':
            # Yetkisiz erişim denemesi
            security_logger.log_unauthorized_access(
                endpoint=request.path,
                user_id=result['payload'].get('user_id'),
                required_role='admin'
            )
            logger.warning(
                f'Unauthorized admin access attempt by user {result["payload"].get("user_id")} '
                f'to {request.path}'
            )
            return jsonify({'success': False, 'message': 'Admin yetkisi gerekli'}), 403

        # Başarılı admin erişimi
        logger.info(
            f'Admin access: {request.method} {request.path} '
            f'by user {result["payload"].get("user_id")}'
        )

        return f(result['payload'], *args, **kwargs)

    return decorated
