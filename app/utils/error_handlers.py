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
    def handle_business_logic_error(error):
        """Business logic hatası handler"""
        logger.info(f'Business logic error: {error.message}')
        return jsonify({
            'success': False,
            'error': 'business_error',
            'message': error.message,
            'details': error.details
        }), 422

    @app.errorhandler(DatabaseException)
    def handle_database_error(error):
        """Database hatası handler"""
        logger.error(f'Database error: {error.message}', exc_info=True)
        return jsonify({
            'success': False,
            'error': 'database_error',
            'message': 'Veritabanı hatası oluştu'
        }), 500

    @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(error):
        """SQLAlchemy generic error handler"""
        logger.error(f'SQLAlchemy error: {str(error)}', exc_info=True)
        return jsonify({
            'success': False,
            'error': 'database_error',
            'message': 'Veritabanı hatası oluştu'
        }), 500

    @app.errorhandler(LibraryException)
    def handle_library_error(error):
        """Generic library exception handler"""
        logger.error(f'Library error: {error.message}', extra={'details': error.details})
        return jsonify({
            'success': False,
            'error': error.error_code or 'library_error',
            'message': error.message
        }), 500

    @app.errorhandler(404)
    def handle_404(error):
        """404 Not Found handler"""
        return jsonify({
            'success': False,
            'error': 'not_found',
            'message': 'Sayfa bulunamadı'
        }), 404

    @app.errorhandler(500)
    def handle_500(error):
        """500 Internal Server Error handler"""
        logger.error(f'Internal server error: {str(error)}', exc_info=True)
        return jsonify({
            'success': False,
            'error': 'internal_server_error',
            'message': 'Sunucu hatası oluştu'
        }), 500

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        """Unexpected error handler"""
        logger.critical(f'Unexpected error: {str(error)}', exc_info=True)

        # Production'da detay gösterme
        if app.config.get('DEBUG'):
            message = str(error)
        else:
            message = 'Beklenmeyen bir hata oluştu'

        return jsonify({
            'success': False,
            'error': 'unexpected_error',
            'message': message
        }), 500

    logger.info('Error handlers registered successfully')
