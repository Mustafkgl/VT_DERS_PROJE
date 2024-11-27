from app.models.user import db
from datetime import datetime

class Fine(db.Model):
    """Ceza Entity"""
    __tablename__ = 'fines'

    id = db.Column(db.Integer, primary_key=True)