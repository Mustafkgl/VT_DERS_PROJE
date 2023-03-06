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
        """Test book search functionality"""
        with app.app_context():
            # Create test books
            BookService.create_book('Clean Code', 'Robert Martin')
            BookService.create_book('Design Patterns', 'Gang of Four')
            BookService.create_book('Refactoring', 'Martin Fowler')

            # Search by title
            result = BookService.search_books('Clean')
            assert result['success'] is True
            assert len(result['books']) == 1
            assert result['books'][0]['title'] == 'Clean Code'

            # Search by author
            result = BookService.search_books('Martin')
            assert result['success'] is True
            assert len(result['books']) >= 2  # Clean Code and Refactoring

    def test_get_available_books(self, app, db_session):
        """Test getting available books"""
        with app.app_context():
            # Create books
            BookService.create_book('Book 1', 'Author 1', total_copies=3)
            BookService.create_book('Book 2', 'Author 2', total_copies=0)

            result = BookService.get_available_books()

            assert result['success'] is True
            assert len(result['books']) == 1
            assert result['books'][0]['title'] == 'Book 1'

    def test_update_book(self, app, db_session):
        """Test book update"""
        with app.app_context():
            # Create book
            create_result = BookService.create_book('Original Title', 'Original Author')
            book_id = create_result['book']['id']

            # Update book
            result = BookService.update_book(
                book_id,
                title='Updated Title',
                author='Updated Author'
            )

            assert result['success'] is True
            assert result['book']['title'] == 'Updated Title'
            assert result['book']['author'] == 'Updated Author'

    def test_delete_book(self, app, db_session):
        """Test book deletion"""
        with app.app_context():
            # Create book
            create_result = BookService.create_book('Test Book', 'Test Author')
            book_id = create_result['book']['id']

            # Delete book
            result = BookService.delete_book(book_id)

            assert result['success'] is True

            # Verify deletion
            get_result = BookService.get_book(book_id)
            assert get_result['success'] is False
