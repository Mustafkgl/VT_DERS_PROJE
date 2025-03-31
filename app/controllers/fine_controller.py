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
