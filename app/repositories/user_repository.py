from app.models import db, User
from sqlalchemy.exc import IntegrityError

class UserRepository:
    """Kullanıcı Veritabanı Erişim Katmanı"""

    @staticmethod
    def create(username, email, password, role='member'):
        """Yeni kullanıcı oluştur"""
        try:
            user = User(username=username, email=email, role=role)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            return None

    @staticmethod
    def find_by_id(user_id):
        """ID ile kullanıcı bul"""
        return User.query.get(user_id)

    @staticmethod
    def find_by_username(username):
        """Kullanıcı adı ile kullanıcı bul"""
        return User.query.filter_by(username=username).first()

    @staticmethod
    def find_by_email(email):
        """Email ile kullanıcı bul"""
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        """Tüm kullanıcıları getir"""
        return User.query.all()

    @staticmethod
    def update(user):
        """Kullanıcı güncelle"""
        try:
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            return None

    @staticmethod
    def delete(user):
        """Kullanıcı sil"""
        try:
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False
