from app.models import db, Fine

class FineRepository:
    """Ceza Veritabanı Erişim Katmanı"""

    @staticmethod
    def find_by_id(fine_id):
        """ID ile ceza bul"""
        return Fine.query.get(fine_id)

    @staticmethod
    def find_by_user(user_id):
        """Kullanıcının tüm cezalarını getir"""
        return Fine.query.filter_by(user_id=user_id).all()

    @staticmethod
    def find_unpaid_by_user(user_id):
        """Kullanıcının ödenmemiş cezalarını getir"""
        return Fine.query.filter_by(user_id=user_id, paid=False).all()

    @staticmethod
    def find_by_borrowing(borrowing_id):
        """Ödünç alma kaydına ait cezayı getir"""
        return Fine.query.filter_by(borrowing_id=borrowing_id).first()

    @staticmethod
    def get_all():