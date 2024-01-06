"""
Rate Limiting Configuration
Brute force ve DDoS saldırılarına karşı koruma
"""
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def get_limiter():
    """
    Rate limiter yapılandırması
