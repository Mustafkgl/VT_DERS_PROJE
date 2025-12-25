"""
Pytest configuration and fixtures
"""

import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.models import db
from config import Config


class TestConfig(Config):
    """Test configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for tests
    SECRET_KEY = 'test-secret-key'
    WTF_CSRF_ENABLED = False


@pytest.fixture(scope='function')
def app():
    """Create application for testing"""
    app = create_app()
    app.config.from_object(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def client(app):
    """Flask test client"""
    return app.test_client()


@pytest.fixture(scope='function')
def runner(app):
    """Flask CLI runner"""
    return app.test_cli_runner()


@pytest.fixture(scope='function')
def db_session(app):
    """Database session for tests"""
    with app.app_context():
        yield db.session
