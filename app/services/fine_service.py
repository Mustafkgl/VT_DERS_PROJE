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
            'fines': [fine.to_dict() for fine in fines]
        }

    @staticmethod
    def pay_fine(fine_id):
        """Cezayı öde"""
        logger.info(f'Fine payment attempt for fine ID: {fine_id}')

        # Önce fine'ı al (bilgileri loglamak için)
        from app.repositories.fine_repository import FineRepository as FR
        fine_before = FR.find_by_id(fine_id)

        if not fine_before:
            logger.warning(f'Fine payment failed: Fine not found - ID {fine_id}')
            return {'success': False, 'message': 'Ceza bulunamadı'}

        if fine_before.paid:
            logger.warning(f'Fine payment failed: Fine already paid - ID {fine_id}')
            return {'success': False, 'message': 'Ceza zaten ödendi'}

        fine = FineRepository.mark_as_paid(fine_id)
        if fine:
            # Data access logging
            security_logger.log_data_access(fine.borrowing.user_id, 'fine', fine_id, 'update')
            logger.info(
                f'Fine paid successfully: Fine ID {fine_id}, '
                f'Amount: {fine.amount}, User ID: {fine.borrowing.user_id}, '
                f'Borrowing ID: {fine.borrowing_id}'
            )
            return {
                'success': True,
                'message': 'Ceza ödendi',
                'fine': fine.to_dict()
            }

        logger.error(f'Fine payment failed: Database error for fine ID {fine_id}')
        return {'success': False, 'message': 'Ceza bulunamadı'}

    @staticmethod
    def get_fine_by_borrowing(borrowing_id):
        """Ödünç alma kaydına ait cezayı getir"""
        fine = FineRepository.find_by_borrowing(borrowing_id)
        if fine:
            return {
                'success': True,
                'fine': fine.to_dict()
            }
        return {'success': False, 'message': 'Ceza bulunamadı'}
