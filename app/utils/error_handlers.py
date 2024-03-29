"""
Global Error Handlers
Flask application için global exception handling
"""

from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
from app.utils.exceptions import (
    LibraryException,
    DatabaseException,
    ValidationException,
    AuthenticationException,
    AuthorizationException,
    ResourceNotFoundException,
    BusinessLogicException,
    ConflictException
)
import logging

logger = logging.getLogger(__name__)


def register_error_handlers(app):
    """Register all error handlers to Flask app"""

    @app.errorhandler(ValidationException)
    def handle_validation_error(error):
        """Validation hatası handler"""
        logger.warning(f'Validation error: {error.message}', extra={'details': error.details})
        return jsonify({
            'success': False,
            'error': 'validation_error',
            'message': error.message,
            'details': error.details
        }), 400

    @app.errorhandler(AuthenticationException)
    def handle_authentication_error(error):