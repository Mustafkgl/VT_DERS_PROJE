"""
Rate Limiting Configuration
Brute force ve DDoS saldırılarına karşı koruma
"""
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def get_limiter():
    """
    Rate limiter yapılandırması

    Limitler:
    - Genel: 200 istek/dakika
    - Login: 5 başarısız deneme/dakika
    - Register: 3 kayıt/saat
    - API: 100 istek/dakika
    """
    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["200 per minute"],
        storage_uri="memory://",
        strategy="fixed-window",
        headers_enabled=True,
    )
    return limiter


# Endpoint-specific rate limiting decorators
def login_limit():
    """Login endpoint için rate limit: 5 deneme/dakika"""
    return "5 per minute"


def register_limit():
    """Register endpoint için rate limit: 3 kayıt/saat"""