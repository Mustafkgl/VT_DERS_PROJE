from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """Kullanıcı Entity"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin' or 'member'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # İlişkiler
    borrowings = db.relationship('Borrowing', back_populates='user', lazy='dynamic')
    fines = db.relationship('Fine', back_populates='user', lazy='dynamic')

    def set_password(self, password):
        """Şifreyi hash'le ve kaydet"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Şifreyi kontrol et"""
        return check_password_hash(self.password, password)

    def to_dict(self):
        """Modeli dictionary'ye çevir"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<User {self.username}>'
