"""
Custom Exception Classes
Daha iyi error handling ve logging için özel exception'lar
"""


class LibraryException(Exception):
    """Base exception for library application"""
    def __init__(self, message, error_code=None, details=None):
        self.message = message
        self.error_code = error_code
        self.details = details or {}
        super().__init__(self.message)

