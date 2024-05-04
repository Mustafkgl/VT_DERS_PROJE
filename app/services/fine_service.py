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