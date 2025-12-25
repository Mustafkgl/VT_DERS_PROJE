from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """Kullanıcı kaydı"""
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'member')

    if not all([username, email, password]):
        return jsonify({'success': False, 'message': 'Eksik bilgi'}), 400

    result = AuthService.register(username, email, password, role)

    if result['success']:
        return jsonify(result), 201
    return jsonify(result), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    """Kullanıcı girişi"""
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return jsonify({'success': False, 'message': 'Eksik bilgi'}), 400

    result = AuthService.login(username, password)

    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 401

@auth_bp.route('/verify', methods=['POST'])
def verify():
    """Token doğrula"""
    data = request.get_json()
    token = data.get('token')

    if not token:
        return jsonify({'success': False, 'message': 'Token gerekli'}), 400

    result = AuthService.verify_token(token)
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 401
