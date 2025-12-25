from app.models.user import db
from datetime import datetime

class Fine(db.Model):
    """Ceza Entity"""
    __tablename__ = 'fines'

    id = db.Column(db.Integer, primary_key=True)
    borrowing_id = db.Column(db.Integer, db.ForeignKey('borrowings.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    paid = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # İlişkiler
    borrowing = db.relationship('Borrowing', back_populates='fine')
    user = db.relationship('User', back_populates='fines')

    def to_dict(self):
        """Modeli dictionary'ye çevir"""
        return {
            'id': self.id,
            'borrowing_id': self.borrowing_id,
            'user_id': self.user_id,
            'amount': float(self.amount),
            'paid': self.paid,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Fine {self.id}>'
