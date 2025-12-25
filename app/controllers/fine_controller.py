from flask import Blueprint, request, jsonify
from app.services.fine_service import FineService
from app.controllers.middleware import token_required, admin_required
import logging

logger = logging.getLogger(__name__)

fine_bp = Blueprint('fine', __name__, url_prefix='/api/fines')

@fine_bp.route('/my', methods=['GET'])
@token_required
def get_my_fines(current_user):
    """Kendi cezalarımı getir"""
    result = FineService.get_user_fines(current_user['user_id'])
    return jsonify(result), 200

@fine_bp.route('/my/unpaid', methods=['GET'])
@token_required
def get_my_unpaid_fines(current_user):
    """Ödenmemiş cezalarımı getir"""
    result = FineService.get_unpaid_fines(current_user['user_id'])
    return jsonify(result), 200

@fine_bp.route('/<int:fine_id>/pay', methods=['POST'])
@token_required
def pay_fine(current_user, fine_id):
    """Ceza öde"""
    result = FineService.pay_fine(fine_id)

    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400

@fine_bp.route('', methods=['GET'])
@admin_required
def get_all_fines(current_user):
    """Tüm cezaları getir (Admin)"""
    result = FineService.get_all_fines()
    return jsonify(result), 200

@fine_bp.route('/unpaid', methods=['GET'])
@admin_required
def get_all_unpaid_fines(current_user):
    """Tüm ödenmemiş cezaları getir (Admin)"""
    result = FineService.get_all_unpaid_fines()
    return jsonify(result), 200
