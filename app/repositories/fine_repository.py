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