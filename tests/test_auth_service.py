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
        with app.app_context():
            # First registration
            AuthService.register('testuser', 'test1@example.com', 'pass123')

            # Second registration with same username
            result = AuthService.register('testuser', 'test2@example.com', 'pass456')

            assert result['success'] is False
            assert 'zaten kullanımda' in result['message']

    def test_register_invalid_email(self, app, db_session):
        """Test registration with invalid email"""
        with app.app_context():
            result = AuthService.register(
                username='testuser',
                email='invalid-email',
                password='pass123'
            )

            assert result['success'] is False
            assert 'Geçersiz email' in result['message']

    def test_register_weak_password(self, app, db_session):
        """Test registration with weak password"""
        with app.app_context():
            result = AuthService.register(
                username='testuser',
                email='test@example.com',
                password='123'  # Too short
            )