from app.repositories.book_repository import BookRepository
from app.utils.validators import InputValidator
from app.utils.security_logger import security_logger
from sqlalchemy.exc import IntegrityError
import logging

logger = logging.getLogger(__name__)

class BookService:
    """Kitap İş Mantığı"""

    @staticmethod
    def create_book(title, author, isbn=None, publisher=None,
                   publication_year=None, total_copies=1):
        """Yeni kitap ekle"""
        logger.info(f'Book creation attempt: {title} by {author}')

        # Input validation
        if not title or not author:
            logger.warning('Book creation failed: Missing title or author')
            return {'success': False, 'message': 'Başlık ve yazar gerekli'}

        # Girdi temizleme (XSS koruması)
        title = InputValidator.sanitize_text(title, max_length=200)
        author = InputValidator.sanitize_text(author, max_length=100)

        if publisher:
            publisher = InputValidator.sanitize_text(publisher, max_length=100)

        # ISBN kontrolü
        if isbn:
            if not InputValidator.validate_isbn(isbn):
                security_logger.log_validation_error('isbn', isbn, 'Invalid ISBN format')
                logger.warning(f'Book creation failed: Invalid ISBN format - {isbn}')
                return {'success': False, 'message': 'Geçersiz ISBN formatı'}
            isbn = InputValidator.sanitize_text(isbn, max_length=20)
            # ISBN duplicate check'i database constraint'e bırakıyoruz (race condition önlemek için)

        # Yıl kontrolü
        if publication_year and not InputValidator.validate_year(publication_year):
            security_logger.log_validation_error('publication_year', publication_year, 'Invalid year')
            logger.warning(f'Book creation failed: Invalid publication year - {publication_year}')
            return {'success': False, 'message': 'Geçersiz yayın yılı'}