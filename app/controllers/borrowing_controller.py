from flask import Blueprint, request, jsonify
from app.services.borrowing_service import BorrowingService
from app.controllers.middleware import token_required, admin_required
from app.utils.security_logger import security_logger
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

borrowing_bp = Blueprint('borrowing', __name__, url_prefix='/api/borrowings')

@borrowing_bp.route('', methods=['POST'])
@token_required
def borrow_book(current_user):
    """Kitap ödünç al"""
    data = request.get_json()
    book_id = data.get('book_id')
    days = data.get('days', 14)

    if not book_id:
        return jsonify({'success': False, 'message': 'Kitap ID gerekli'}), 400

    result = BorrowingService.borrow_book(current_user['user_id'], book_id, days)

    if result['success']:
        return jsonify(result), 201
    return jsonify(result), 400

@borrowing_bp.route('/<int:borrowing_id>/return', methods=['POST'])
@token_required
def return_book(current_user, borrowing_id):
    """Kitap iade et"""
    result = BorrowingService.return_book(borrowing_id)

    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400

@borrowing_bp.route('/my', methods=['GET'])
@token_required
def get_my_borrowings(current_user):
    """Kendi ödünç kayıtlarımı getir"""
    result = BorrowingService.get_user_borrowings(current_user['user_id'])
    return jsonify(result), 200