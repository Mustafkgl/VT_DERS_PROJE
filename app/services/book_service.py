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

        # Kopya sayısı kontrolü
        if not InputValidator.validate_positive_integer(total_copies, min_value=1, max_value=1000):
            security_logger.log_validation_error('total_copies', total_copies, 'Invalid copy count')
            logger.warning(f'Book creation failed: Invalid copy count - {total_copies}')
            return {'success': False, 'message': 'Geçersiz kopya sayısı (1-1000 arası olmalı)'}

        try:
            book = BookRepository.create(
                title=title,
                author=author,
                isbn=isbn,
                publisher=publisher,
                publication_year=publication_year,
                total_copies=total_copies,
                available_copies=total_copies
            )

            if book:
                logger.info(f'Book created successfully: {title} (ID: {book.id}, ISBN: {isbn or "N/A"})')
                return {'success': True, 'message': 'Kitap eklendi', 'book': book.to_dict()}

            logger.error(f'Book creation failed: Database error for {title}')
            return {'success': False, 'message': 'Kitap eklenemedi'}

        except IntegrityError as e:
            # ISBN duplicate veya diğer constraint violation
            logger.warning(f'Book creation failed: Integrity constraint violation - {str(e)}')
            if isbn and 'isbn' in str(e).lower():
                return {'success': False, 'message': 'Bu ISBN zaten kayıtlı'}
            return {'success': False, 'message': 'Kitap eklenemedi (veri bütünlüğü hatası)'}

    @staticmethod
    def get_book(book_id):
        """Kitap detayını getir"""
        logger.debug(f'Fetching book details for ID: {book_id}')
        book = BookRepository.find_by_id(book_id)
        if book:
            logger.debug(f'Book found: {book.title} (ID: {book_id})')
            return {'success': True, 'book': book.to_dict()}
        logger.warning(f'Book not found: ID {book_id}')
        return {'success': False, 'message': 'Kitap bulunamadı'}

    @staticmethod
    def get_all_books(page: int = 1, per_page: int = 10):
        """Tüm kitapları getir (paginated)"""
        from app.models import Book

        # Pagination
        pagination = Book.query.order_by(Book.id.desc()).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        return {
            'success': True,
            'books': [book.to_dict() for book in pagination.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': pagination.total,
                'pages': pagination.pages,
                'has_next': pagination.has_next,
                'has_prev': pagination.has_prev
            }
        }

    @staticmethod
    def get_available_books():
        """Mevcut kitapları getir"""
        books = BookRepository.get_available()
        return {
            'success': True,
            'books': [book.to_dict() for book in books]
        }

    @staticmethod
    def search_books(query):
        """Kitap ara"""
        logger.info(f'Book search query: {query}')
        books = BookRepository.search(query)
        logger.info(f'Book search returned {len(books)} results for query: {query}')
        return {
            'success': True,
            'books': [book.to_dict() for book in books]
        }

    @staticmethod
    def update_book(book_id, **kwargs):
        """Kitap güncelle"""
        logger.info(f'Book update attempt for ID: {book_id}')
        book = BookRepository.find_by_id(book_id)
        if not book:
            logger.warning(f'Book update failed: Book not found - ID {book_id}')
            return {'success': False, 'message': 'Kitap bulunamadı'}

        # Güncellenebilir alanlar
        updatable_fields = ['title', 'author', 'isbn', 'publisher',
                           'publication_year', 'total_copies']

        updated_fields = []
        for field in updatable_fields:
            if field in kwargs:
                setattr(book, field, kwargs[field])
                updated_fields.append(field)

        updated_book = BookRepository.update(book)
        if updated_book:
            logger.info(f'Book updated successfully: {book.title} (ID: {book_id}, Fields: {", ".join(updated_fields)})')
            return {'success': True, 'message': 'Kitap güncellendi', 'book': updated_book.to_dict()}

        logger.error(f'Book update failed: Database error for ID {book_id}')
        return {'success': False, 'message': 'Güncelleme başarısız'}

    @staticmethod
    def delete_book(book_id):
        """Kitap sil"""
        logger.info(f'Book deletion attempt for ID: {book_id}')
        book = BookRepository.find_by_id(book_id)
        if not book:
            logger.warning(f'Book deletion failed: Book not found - ID {book_id}')
            return {'success': False, 'message': 'Kitap bulunamadı'}

        book_title = book.title
        if BookRepository.delete(book):
            logger.info(f'Book deleted successfully: {book_title} (ID: {book_id})')
            return {'success': True, 'message': 'Kitap silindi'}

        logger.error(f'Book deletion failed: Database error for ID {book_id}')
        return {'success': False, 'message': 'Silme başarısız'}
