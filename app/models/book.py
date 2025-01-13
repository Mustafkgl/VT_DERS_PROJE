from app.models.user import db
from datetime import datetime

class Book(db.Model):
    """Kitap Entity"""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)