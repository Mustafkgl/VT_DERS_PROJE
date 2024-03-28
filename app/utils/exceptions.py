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


class DatabaseException(LibraryException):
    """Database operation hatası"""
    def __init__(self, message, details=None):
        super().__init__(message, error_code='DB_ERROR', details=details)


class ValidationException(LibraryException):
    """Input validation hatası"""
    def __init__(self, message, field=None, details=None):
        details = details or {}
        if field:
            details['field'] = field
        super().__init__(message, error_code='VALIDATION_ERROR', details=details)


class AuthenticationException(LibraryException):
    """Authentication hatası"""
    def __init__(self, message, details=None):
        super().__init__(message, error_code='AUTH_ERROR', details=details)


class AuthorizationException(LibraryException):
    """Authorization hatası"""
    def __init__(self, message, details=None):
        super().__init__(message, error_code='AUTHZ_ERROR', details=details)


class ResourceNotFoundException(LibraryException):
    """Kaynak bulunamadı hatası"""
    def __init__(self, resource_type, resource_id, details=None):
        message = f'{resource_type} bulunamadı (ID: {resource_id})'
        details = details or {}
        details['resource_type'] = resource_type
        details['resource_id'] = resource_id
        super().__init__(message, error_code='NOT_FOUND', details=details)


class BusinessLogicException(LibraryException):
    """İş mantığı hatası (stok yok, gecikmiş iade vb.)"""
    def __init__(self, message, details=None):
        super().__init__(message, error_code='BUSINESS_ERROR', details=details)


class ConflictException(LibraryException):
    """Veri çakışması hatası (duplicate ISBN vb.)"""
    def __init__(self, message, details=None):
        super().__init__(message, error_code='CONFLICT', details=details)
