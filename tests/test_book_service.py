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