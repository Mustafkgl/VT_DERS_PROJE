from app.models import db, Book
from sqlalchemy.exc import IntegrityError

class BookRepository:
    """Kitap Veritabanı Erişim Katmanı"""

    @staticmethod
    def create(title, author, isbn=None, publisher=None, publication_year=None,
               total_copies=1, available_copies=1):
        """Yeni kitap oluştur"""
        try:
            book = Book(
                title=title,
                author=author,
                isbn=isbn,
                publisher=publisher,
                publication_year=publication_year,
                total_copies=total_copies,
                available_copies=available_copies
            )
            db.session.add(book)
            db.session.commit()
            return book
        except IntegrityError:
            db.session.rollback()