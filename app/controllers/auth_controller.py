from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
from app import limiter

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
@limiter.limit("3 per hour")  # Rate limiting: 3 kayıt/saat
def register():
    """Kullanıcı kaydı"""
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')