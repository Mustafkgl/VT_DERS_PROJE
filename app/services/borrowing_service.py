from datetime import datetime, timedelta
from app.repositories.borrowing_repository import BorrowingRepository
from app.repositories.book_repository import BookRepository
from app.repositories.user_repository import UserRepository
from app.utils.security_logger import security_logger
from app.models import db
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

class BorrowingService:
    """Ödünç Alma İş Mantığı"""

    @staticmethod
    def borrow_book(user_id, book_id, days=14):
        """Kitap ödünç al - Atomic transaction"""
        logger.info(f'Borrow attempt: User {user_id} requesting Book {book_id}')

        # Kullanıcı kontrolü
        user = UserRepository.find_by_id(user_id)
        if not user:
            logger.warning(f'Borrow failed: User not found - ID {user_id}')
            return {'success': False, 'message': 'Kullanıcı bulunamadı'}

        # Kitap kontrolü
        book = BookRepository.find_by_id(book_id)
        if not book:
            logger.warning(f'Borrow failed: Book not found - ID {book_id}')
            return {'success': False, 'message': 'Kitap bulunamadı'}

        # Stok kontrolü
        if book.available_copies <= 0:
            logger.warning(f'Borrow failed: Book out of stock - {book.title} (ID: {book_id})')
            return {'success': False, 'message': 'Kitap stokta yok'}

        # ATOMIC TRANSACTION - Borrowing create ve stok azaltma tek transaction'da
        try:
            # Ödünç alma kaydı oluştur (commit yapmadan)
            due_date = datetime.utcnow() + timedelta(days=days)
            borrowing = BorrowingRepository.create(user_id, book_id, due_date, auto_commit=False)

            if not borrowing:
                raise SQLAlchemyError("Failed to create borrowing record")

            # Kitap stok sayısını azalt (commit yapmadan)
            stock_decreased = BookRepository.decrease_available_copies(book_id, auto_commit=False)