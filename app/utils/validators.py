import re
from html import escape


class PasswordValidator:
    """Şifre güvenliği validasyonu"""

    # Yaygın zayıf şifreler blacklist
    COMMON_PASSWORDS = {
        'password', 'password123', '123456', '12345678', 'qwerty',
        'abc123', 'monkey', '1234567', 'letmein', 'trustno1',
        'dragon', 'baseball', 'iloveyou', 'master', 'sunshine',
        'ashley', 'bailey', 'passw0rd', 'shadow', '123123',
        'admin', 'admin123', 'root', 'test', 'test123'
    }

    @staticmethod
    def validate_password(password):
        """
        Güçlü şifre kontrolü

        Gereksinimler:
        - En az 8 karakter
        - En az 1 büyük harf
        - En az 1 küçük harf
        - En az 1 rakam
        - En az 1 özel karakter
        - Yaygın şifre olmamalı

        Returns:
            tuple: (is_valid: bool, error_message: str)
        """
        if not password:
            return False, 'Şifre boş olamaz'

        if len(password) < 8:
            return False, 'Şifre en az 8 karakter olmalı'

        if len(password) > 128: