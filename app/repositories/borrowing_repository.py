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