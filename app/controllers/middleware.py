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