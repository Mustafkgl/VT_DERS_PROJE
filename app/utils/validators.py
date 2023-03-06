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

        # Maksimum uzunluk kontrolü
        if max_length and len(sanitized) > max_length:
            sanitized = sanitized[:max_length]

        return sanitized

    @staticmethod
    def validate_email(email):
        """Email formatı kontrolü"""
        if not email:
            return False

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))

    @staticmethod
    def validate_username(username):
        """
        Kullanıcı adı kontrolü
        - 3-50 karakter
        - Sadece harf, rakam, alt çizgi ve tire
        """
        if not username or len(username) < 3 or len(username) > 50:
            return False

        username_pattern = r'^[a-zA-Z0-9_-]+$'
        return bool(re.match(username_pattern, username))

    @staticmethod
    def validate_isbn(isbn):
        """ISBN formatı kontrolü (ISBN-10 veya ISBN-13)"""
        if not isbn:
            return True  # ISBN opsiyonel

        # Sadece rakam ve tire
        isbn_clean = isbn.replace('-', '').replace(' ', '')

        # ISBN-10 veya ISBN-13
        if len(isbn_clean) not in [10, 13]:
            return False

        return isbn_clean.isdigit()

    @staticmethod
    def validate_year(year):
        """Yıl kontrolü (1000-2100 arası)"""
        if not year:
            return True  # Yıl opsiyonel

        try:
            year_int = int(year)
            return 1000 <= year_int <= 2100
        except (ValueError, TypeError):
            return False

    @staticmethod
    def validate_positive_integer(value, min_value=1, max_value=None):
        """Pozitif tamsayı kontrolü"""
        try:
            int_value = int(value)
            if int_value < min_value:
                return False
            if max_value and int_value > max_value:
                return False
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def remove_html_tags(text):
        """HTML taglerini kaldır"""
        if not text:
            return text

        # HTML taglerini temizle
        clean_text = re.sub(r'<[^>]+>', '', str(text))
        return clean_text.strip()
