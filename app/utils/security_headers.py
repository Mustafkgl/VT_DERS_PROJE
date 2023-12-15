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