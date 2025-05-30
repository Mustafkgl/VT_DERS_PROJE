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
    total_copies = data.get('total_copies', 1)

    if not all([title, author]):
        return jsonify({'success': False, 'message': 'Başlık ve yazar gerekli'}), 400

    result = BookService.create_book(
        title=title,
        author=author,
        isbn=isbn,
        publisher=publisher,
        publication_year=publication_year,
        total_copies=total_copies
    )

    if result['success']:
        # Admin action logging
        book_id = result['book']['id']
        security_logger.log_admin_action(
            admin_id=current_user['user_id'],
            action='create_book',
            target_type='book',
            target_id=book_id,
            details={'title': title, 'author': author, 'isbn': isbn}
        )
        return jsonify(result), 201
    return jsonify(result), 400

@book_bp.route('/<int:book_id>', methods=['PUT'])
@admin_required
def update_book(current_user, book_id):
    """Kitap güncelle (Admin)"""
    data = request.get_json()
    result = BookService.update_book(book_id, **data)

    if result['success']:
        # Admin action logging
        security_logger.log_admin_action(
            admin_id=current_user['user_id'],
            action='update_book',
            target_type='book',
            target_id=book_id,
            details={'updated_fields': list(data.keys())}
        )
        return jsonify(result), 200
    return jsonify(result), 400

@book_bp.route('/<int:book_id>', methods=['DELETE'])
@admin_required
def delete_book(current_user, book_id):
    """Kitap sil (Admin)"""
    result = BookService.delete_book(book_id)

    if result['success']:
        # Admin action logging
        security_logger.log_admin_action(
            admin_id=current_user['user_id'],
            action='delete_book',
            target_type='book',
            target_id=book_id
        )
        return jsonify(result), 200
    return jsonify(result), 400
