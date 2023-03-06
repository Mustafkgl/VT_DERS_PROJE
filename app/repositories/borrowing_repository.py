from app.models import db, Borrowing
from datetime import datetime
from sqlalchemy import text

class BorrowingRepository:
    """Ödünç Alma Veritabanı Erişim Katmanı"""

    @staticmethod
    def create(user_id, book_id, due_date, auto_commit=True):
        """Yeni ödünç alma kaydı oluştur"""
        try:
            borrowing = Borrowing(
                user_id=user_id,
                book_id=book_id,
                due_date=due_date,
                status='borrowed'
            )
            db.session.add(borrowing)
            if auto_commit:
                db.session.commit()
            else:
                db.session.flush()  # Get ID without committing
            return borrowing
        except Exception:
            db.session.rollback()
            return None

    @staticmethod
    def find_by_id(borrowing_id):
        """ID ile ödünç alma kaydı bul"""
        return Borrowing.query.get(borrowing_id)

    @staticmethod
    def find_by_user(user_id):
        """Kullanıcının tüm ödünç alma kayıtlarını getir"""
        return Borrowing.query.filter_by(user_id=user_id).all()

    @staticmethod
    def find_active_by_user(user_id):
        """Kullanıcının aktif ödünç alma kayıtlarını getir"""
        return Borrowing.query.filter_by(
            user_id=user_id,
            status='borrowed'
        ).all()

    @staticmethod
    def find_by_book(book_id):
        """Kitabın tüm ödünç alma kayıtlarını getir"""
        return Borrowing.query.filter_by(book_id=book_id).all()

    @staticmethod
    def get_all():
        """Tüm ödünç alma kayıtlarını getir"""
        return Borrowing.query.all()

    @staticmethod
    def get_active():
        """Aktif ödünç alma kayıtlarını getir"""
        return Borrowing.query.filter_by(status='borrowed').all()

    @staticmethod
    def return_book(borrowing_id, return_date=None):
        """Kitap iadesi yap - Trigger otomatik ceza hesaplayacak"""
        borrowing = Borrowing.query.get(borrowing_id)
        if borrowing and borrowing.status == 'borrowed':
            borrowing.return_date = return_date or datetime.utcnow()
            # Trigger burada devreye girecek ve ceza hesaplayacak
            db.session.commit()
            return borrowing
        return None

    @staticmethod
    def update(borrowing):
        """Ödünç alma kaydı güncelle"""
        try:
            db.session.commit()
            return borrowing
        except Exception:
            db.session.rollback()
            return None

    @staticmethod
    def get_report(start_date, end_date):
        """Stored Procedure ile rapor al"""
        sql = text("""
            SELECT * FROM get_borrowings_report(:start_date, :end_date)
        """)
        result = db.session.execute(
            sql,
            {'start_date': start_date, 'end_date': end_date}
        )
        return result.fetchall()
