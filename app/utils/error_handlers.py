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
        """Authentication hatası handler"""
        logger.warning(f'Authentication error: {error.message}')
        return jsonify({
            'success': False,
            'error': 'authentication_error',
            'message': error.message
        }), 401

    @app.errorhandler(AuthorizationException)
    def handle_authorization_error(error):
        """Authorization hatası handler"""
        logger.warning(f'Authorization error: {error.message}', extra={'details': error.details})
        return jsonify({
            'success': False,
            'error': 'authorization_error',
            'message': error.message
        }), 403

    @app.errorhandler(ResourceNotFoundException)
    def handle_not_found_error(error):
        """Resource not found hatası handler"""
        logger.info(f'Resource not found: {error.message}')
        return jsonify({
            'success': False,
            'error': 'not_found',
            'message': error.message
        }), 404

    @app.errorhandler(ConflictException)
    def handle_conflict_error(error):
        """Conflict hatası handler"""
        logger.warning(f'Conflict error: {error.message}', extra={'details': error.details})
        return jsonify({
            'success': False,
            'error': 'conflict',
            'message': error.message
        }), 409

    @app.errorhandler(BusinessLogicException)