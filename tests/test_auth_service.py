"""
Auth Service Unit Tests
"""

import pytest
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository


class TestAuthService:
    """Authentication service test cases"""

    def test_register_success(self, app, db_session):
        """Test successful user registration"""
        with app.app_context():
            result = AuthService.register(
                username='testuser',
                email='test@example.com',
                password='test123',
                role='member'
            )

            assert result['success'] is True
            assert result['message'] == 'Kayıt başarılı'
            assert 'user' in result
            assert result['user']['username'] == 'testuser'

    def test_register_duplicate_username(self, app, db_session):
        """Test registration with duplicate username"""