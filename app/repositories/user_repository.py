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