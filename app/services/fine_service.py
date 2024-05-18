from app.repositories.fine_repository import FineRepository
from app.utils.security_logger import security_logger
import logging

logger = logging.getLogger(__name__)

class FineService:
    """Ceza İş Mantığı"""

    @staticmethod
    def get_user_fines(user_id):
        """Kullanıcının tüm cezalarını getir"""
        logger.debug(f'Fetching fines for user ID: {user_id}')
        fines = FineRepository.find_by_user(user_id)
        logger.debug(f'Found {len(fines)} fines for user ID: {user_id}')
        return {
            'success': True,
            'fines': [fine.to_dict() for fine in fines]
        }

    @staticmethod
    def get_unpaid_fines(user_id):
        """Kullanıcının ödenmemiş cezalarını getir"""
        logger.debug(f'Fetching unpaid fines for user ID: {user_id}')
        fines = FineRepository.find_unpaid_by_user(user_id)
        total_amount = sum(float(fine.amount) for fine in fines)
        logger.info(f'User {user_id} has {len(fines)} unpaid fines totaling {total_amount}')
        return {
            'success': True,
            'fines': [fine.to_dict() for fine in fines],
            'total_amount': total_amount
        }

    @staticmethod
    def get_all_fines():
        """Tüm cezaları getir"""
        fines = FineRepository.get_all()
        return {
            'success': True,
            'fines': [fine.to_dict() for fine in fines]
        }

    @staticmethod
    def get_all_unpaid_fines():
        """Tüm ödenmemiş cezaları getir"""
        fines = FineRepository.get_unpaid()
        return {
            'success': True,