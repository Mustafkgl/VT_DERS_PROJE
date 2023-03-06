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
            return None

    @staticmethod
    def find_by_id(book_id):
        """ID ile kitap bul"""
        return Book.query.get(book_id)

    @staticmethod
    def find_by_isbn(isbn):
        """ISBN ile kitap bul"""
        return Book.query.filter_by(isbn=isbn).first()

    @staticmethod
    def search(query):
        """Kitap ara (başlık veya yazar)"""
        search_pattern = f'%{query}%'
        return Book.query.filter(
            db.or_(
                Book.title.ilike(search_pattern),
                Book.author.ilike(search_pattern)
            )
        ).all()

    @staticmethod
    def get_all():
        """Tüm kitapları getir"""
        return Book.query.all()

    @staticmethod
    def get_available():
        """Mevcut kitapları getir"""
        return Book.query.filter(Book.available_copies > 0).all()

    @staticmethod
    def update(book):
        """Kitap güncelle"""
        try:
            db.session.commit()
            return book
        except IntegrityError:
            db.session.rollback()
            return None

    @staticmethod
    def delete(book):
        """Kitap sil"""
        try:
            db.session.delete(book)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False

    @staticmethod
    def decrease_available_copies(book_id, auto_commit=True):
        """Mevcut kopya sayısını azalt"""
        book = Book.query.get(book_id)
        if book and book.available_copies > 0:
            book.available_copies -= 1
            if auto_commit:
                db.session.commit()
            return True
        return False

    @staticmethod
    def increase_available_copies(book_id, auto_commit=True):
        """Mevcut kopya sayısını artır"""
        book = Book.query.get(book_id)
        if book and book.available_copies < book.total_copies:
            book.available_copies += 1
            if auto_commit:
                db.session.commit()
            return True
        return False
