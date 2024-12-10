from app.models.user import db
from datetime import datetime

class Borrowing(db.Model):
    """Ödünç Alma Entity"""
    __tablename__ = 'borrowings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)