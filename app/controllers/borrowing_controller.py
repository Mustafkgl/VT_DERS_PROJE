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
