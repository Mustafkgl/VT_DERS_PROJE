from app.models.user import db
from datetime import datetime

class Borrowing(db.Model):
    """Ödünç Alma Entity"""
    __tablename__ = 'borrowings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), nullable=False, default='borrowed')  # 'borrowed', 'returned', 'overdue'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # İlişkiler
    user = db.relationship('User', back_populates='borrowings')
    book = db.relationship('Book', back_populates='borrowings')
    fine = db.relationship('Fine', back_populates='borrowing', uselist=False)

    def to_dict(self):
        """Modeli dictionary'ye çevir"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'book_id': self.book_id,