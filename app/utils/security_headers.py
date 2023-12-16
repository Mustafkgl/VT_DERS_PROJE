"""
Security Headers Middleware
HTTP güvenlik başlıklarını ekler
"""
from flask import Flask

def add_security_headers(app: Flask):
    """
    Flask uygulamasına güvenlik başlıkları ekle

    Eklenen başlıklar:
    - X-Content-Type-Options: MIME type sniffing koruması
    - X-Frame-Options: Clickjacking koruması
    - X-XSS-Protection: XSS koruması (eski tarayıcılar için)
    - Strict-Transport-Security: HTTPS zorunluluğu
    - Content-Security-Policy: XSS ve injection saldırı koruması
    - Referrer-Policy: Referrer bilgisi gizliliği
    """

    @app.after_request
    def set_security_headers(response):
        # MIME type sniffing koruması
        response.headers['X-Content-Type-Options'] = 'nosniff'

        # Clickjacking koruması
        response.headers['X-Frame-Options'] = 'DENY'

        # XSS koruması (eski tarayıcılar için)
        response.headers['X-XSS-Protection'] = '1; mode=block'
