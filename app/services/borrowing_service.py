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

            if not stock_decreased:
                raise SQLAlchemyError("Failed to decrease book stock")

            # Her iki işlem başarılı - commit
            db.session.commit()

            # Data access logging
            security_logger.log_data_access(user_id, 'borrowing', borrowing.id, 'create')
            logger.info(
                f'Book borrowed successfully: {book.title} (ID: {book_id}) '
                f'by user {user.username} (ID: {user_id}), Due: {due_date.date()}'
            )

            return {
                'success': True,
                'message': 'Kitap ödünç alındı',
                'borrowing': borrowing.to_dict()
            }

        except SQLAlchemyError as e:
            # Hata durumunda rollback
            db.session.rollback()
            logger.error(
                f'Borrow failed: Transaction error - User {user_id}, Book {book_id}: {str(e)}',
                exc_info=True
            )
            return {'success': False, 'message': 'Ödünç alma işlemi başarısız'}

    @staticmethod
    def return_book(borrowing_id):
        """Kitap iade et - Atomic transaction"""
        logger.info(f'Return attempt for borrowing ID: {borrowing_id}')
        borrowing = BorrowingRepository.find_by_id(borrowing_id)
        if not borrowing:
            logger.warning(f'Return failed: Borrowing not found - ID {borrowing_id}')
            return {'success': False, 'message': 'Ödünç kaydı bulunamadı'}

        if borrowing.status != 'borrowed':
            logger.warning(f'Return failed: Book already returned - Borrowing ID {borrowing_id}')
            return {'success': False, 'message': 'Kitap zaten iade edilmiş'}

        user_id = borrowing.user_id
        book_id = borrowing.book_id

        # ATOMIC TRANSACTION - İade ve stok artırma tek transaction'da
        try:
            # İade işlemini yap
            borrowing.return_date = datetime.utcnow()
            borrowing.status = 'returned'

            # Kitap stok sayısını artır (commit yapmadan)
            stock_increased = BookRepository.increase_available_copies(book_id, auto_commit=False)

            if not stock_increased:
                raise SQLAlchemyError("Failed to increase book stock")

            # Her iki işlem başarılı - commit (trigger da bu noktada çalışacak)
            db.session.commit()

            # Data access logging
            security_logger.log_data_access(user_id, 'borrowing', borrowing_id, 'update')

            is_late = borrowing.return_date > borrowing.due_date
            logger.info(
                f'Book returned successfully: Borrowing ID {borrowing_id}, '
                f'User ID {user_id}, Book ID {book_id}, '
                f'Late: {is_late}'
            )

            return {
                'success': True,
                'message': 'Kitap iade edildi',
                'borrowing': borrowing.to_dict()
            }

        except SQLAlchemyError as e:
            # Hata durumunda rollback
            db.session.rollback()
            logger.error(
                f'Return failed: Transaction error for borrowing ID {borrowing_id}: {str(e)}',
                exc_info=True
            )
            return {'success': False, 'message': 'İade işlemi başarısız'}

    @staticmethod
    def get_user_borrowings(user_id):
        """Kullanıcının ödünç alma kayıtlarını getir"""
        borrowings = BorrowingRepository.find_by_user(user_id)
        return {
            'success': True,
            'borrowings': [b.to_dict() for b in borrowings]
        }

    @staticmethod
    def get_active_borrowings():
        """Aktif ödünç alma kayıtlarını getir"""
        borrowings = BorrowingRepository.get_active()
        return {
            'success': True,
            'borrowings': [b.to_dict() for b in borrowings]
        }

    @staticmethod
    def get_all_borrowings():
        """Tüm ödünç alma kayıtlarını getir"""
        borrowings = BorrowingRepository.get_all()
        return {
            'success': True,
            'borrowings': [b.to_dict() for b in borrowings]
        }

    @staticmethod
    def get_borrowings_report(start_date, end_date):
        """Stored Procedure ile rapor al"""
        logger.info(f'Generating borrowings report: {start_date} to {end_date}')
        try:
            report = BorrowingRepository.get_report(start_date, end_date)
            # Sonuçları dictionary'ye çevir
            report_data = []
            for row in report:
                report_data.append({
                    'borrowing_id': row[0],
                    'user_name': row[1],
                    'user_email': row[2],
                    'book_title': row[3],
                    'book_author': row[4],
                    'borrow_date': row[5].isoformat() if row[5] else None,
                    'due_date': row[6].isoformat() if row[6] else None,
                    'return_date': row[7].isoformat() if row[7] else None,
                    'status': row[8],
                    'fine_amount': float(row[9]) if row[9] else 0.0,
                    'fine_paid': row[10] if row[10] is not None else False
                })

            logger.info(f'Borrowings report generated successfully: {len(report_data)} records')
            return {
                'success': True,
                'report': report_data
            }
        except Exception as e:
            logger.error(f'Report generation failed: {str(e)}', exc_info=True)
            return {'success': False, 'message': f'Rapor oluşturulamadı: {str(e)}'}
