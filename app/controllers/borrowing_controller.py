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

@borrowing_bp.route('', methods=['GET'])
@admin_required
def get_all_borrowings(current_user):
    """Tüm ödünç kayıtlarını getir (Admin)"""
    result = BorrowingService.get_all_borrowings()
    return jsonify(result), 200

@borrowing_bp.route('/active', methods=['GET'])
@admin_required
def get_active_borrowings(current_user):
    """Aktif ödünç kayıtlarını getir (Admin)"""
    result = BorrowingService.get_active_borrowings()
    return jsonify(result), 200

@borrowing_bp.route('/report', methods=['GET'])
@admin_required
def get_borrowings_report(current_user):
    """Tarih aralığına göre rapor al (Admin) - Stored Procedure kullanır"""
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    if not all([start_date_str, end_date_str]):
        return jsonify({'success': False, 'message': 'Başlangıç ve bitiş tarihi gerekli'}), 400

    try:
        start_date = datetime.fromisoformat(start_date_str)
        end_date = datetime.fromisoformat(end_date_str)
    except ValueError:
        return jsonify({'success': False, 'message': 'Geçersiz tarih formatı (YYYY-MM-DD)'}), 400

    result = BorrowingService.get_borrowings_report(start_date, end_date)

    if result['success']:
        # Admin action logging for report generation
        security_logger.log_admin_action(
            admin_id=current_user['user_id'],
            action='generate_borrowings_report',
            target_type='borrowing',
            target_id=0,  # No specific borrowing
            details={'start_date': start_date_str, 'end_date': end_date_str, 'record_count': len(result.get('report', []))}
        )
        return jsonify(result), 200
    return jsonify(result), 400
