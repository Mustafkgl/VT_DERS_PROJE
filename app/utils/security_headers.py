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

        # HTTPS zorunluluğu (production için)
        # 1 yıl = 31536000 saniye
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'

        # Content Security Policy
        # Self: Sadece kendi domain'den kaynak
        # unsafe-inline: Inline script/style izni (gerekirse kaldırılabilir)
        csp_directives = [
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline'",
            "style-src 'self' 'unsafe-inline'",
            "img-src 'self' data: https:",
            "font-src 'self' data:",
            "connect-src 'self'",
            "frame-ancestors 'none'",
            "base-uri 'self'",
            "form-action 'self'"
        ]
        response.headers['Content-Security-Policy'] = '; '.join(csp_directives)

        # Referrer policy
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'

        # Permissions policy (önceden Feature-Policy)
        response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'

        return response

    return app
