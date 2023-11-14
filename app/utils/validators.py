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
            return False, 'Şifre en fazla 128 karakter olabilir'

        # Büyük harf kontrolü
        if not re.search(r'[A-Z]', password):
            return False, 'Şifre en az 1 büyük harf içermeli'

        # Küçük harf kontrolü
        if not re.search(r'[a-z]', password):
            return False, 'Şifre en az 1 küçük harf içermeli'

        # Rakam kontrolü
        if not re.search(r'\d', password):
            return False, 'Şifre en az 1 rakam içermeli'

        # Özel karakter kontrolü
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False, 'Şifre en az 1 özel karakter içermeli (!@#$%^&*...)'

        # Yaygın şifre kontrolü
        if password.lower() in PasswordValidator.COMMON_PASSWORDS:
            return False, 'Bu şifre çok yaygın kullanılıyor, lütfen daha güçlü bir şifre seçin'

        return True, ''


class InputValidator:
    """Girdi doğrulama ve güvenlik kontrolleri"""

    @staticmethod
    def sanitize_text(text, max_length=None):
        """
        Metni temizle ve XSS saldırılarına karşı koruma sağla
        """
        if not text:
            return text

        # HTML karakterlerini escape et
        sanitized = escape(str(text).strip())
