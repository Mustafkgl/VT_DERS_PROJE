"""
Book Service Unit Tests
"""

import pytest
from app.services.book_service import BookService


class TestBookService:
    """Book service test cases"""

    def test_create_book_success(self, app, db_session):
        """Test successful book creation"""
        with app.app_context():
            result = BookService.create_book(
                title='Clean Code',
                author='Robert C. Martin',
                isbn='978-0132350884',
                publisher='Prentice Hall',
                publication_year=2008,
                total_copies=5
            )

            assert result['success'] is True
            assert result['book']['title'] == 'Clean Code'
            assert result['book']['available_copies'] == 5

    def test_create_book_missing_required_fields(self, app, db_session):
        """Test book creation without required fields"""
        with app.app_context():
            result = BookService.create_book(
                title='',
                author='Some Author'
            )

            assert result['success'] is False
            assert 'gerekli' in result['message']

    def test_create_book_invalid_isbn(self, app, db_session):
        """Test book creation with invalid ISBN"""
        with app.app_context():
            result = BookService.create_book(
                title='Test Book',
                author='Test Author',
                isbn='invalid-isbn'
            )

            assert result['success'] is False
            assert 'ISBN' in result['message']

    def test_create_book_duplicate_isbn(self, app, db_session):
        """Test book creation with duplicate ISBN"""
        with app.app_context():
            isbn = '978-0132350884'

            # First book
            BookService.create_book('Book 1', 'Author 1', isbn=isbn)

            # Second book with same ISBN
            result = BookService.create_book('Book 2', 'Author 2', isbn=isbn)

            assert result['success'] is False
            assert 'zaten kayıtlı' in result['message']

    def test_search_books(self, app, db_session):