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

@book_bp.route('/<int:book_id>', methods=['GET'])
@token_required
def get_book(current_user, book_id):
    """Kitap detayı"""
    result = BookService.get_book(book_id)
    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 404

@book_bp.route('/search', methods=['GET'])
@token_required
def search_books(current_user):
    """Kitap ara"""
    query = request.args.get('q', '')
    if not query:
        return jsonify({'success': False, 'message': 'Arama sorgusu gerekli'}), 400

    result = BookService.search_books(query)
    return jsonify(result), 200

@book_bp.route('', methods=['POST'])
@admin_required
def create_book(current_user):
    """Yeni kitap ekle (Admin)"""
    data = request.get_json()

    title = data.get('title')
    author = data.get('author')
    isbn = data.get('isbn')
    publisher = data.get('publisher')
    publication_year = data.get('publication_year')