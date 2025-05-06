from flask import Blueprint, request, jsonify
from app.services.book_service import BookService
from app.controllers.middleware import token_required, admin_required
from app.utils.security_logger import security_logger
import logging

logger = logging.getLogger(__name__)

book_bp = Blueprint('book', __name__, url_prefix='/api/books')

@book_bp.route('', methods=['GET'])
@token_required
def get_books(current_user):
    """Tüm kitapları getir (with pagination)"""
    # Pagination parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Limit per_page to prevent abuse
    per_page = min(per_page, 100)

    result = BookService.get_all_books(page=page, per_page=per_page)
    return jsonify(result), 200

@book_bp.route('/available', methods=['GET'])
@token_required
def get_available_books(current_user):
    """Mevcut kitapları getir"""
    result = BookService.get_available_books()
    return jsonify(result), 200
