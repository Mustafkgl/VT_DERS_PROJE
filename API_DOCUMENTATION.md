# 📚 Kütüphane Yönetim Sistemi - API Documentation

## Base URL
```
http://localhost:5000/api
```

## Authentication
Tüm API endpoint'leri (login/register hariç) JWT token gerektirir.

**Header:**
```
Authorization: Bearer <your_jwt_token>
```

---

## 1. Authentication Endpoints

### 1.1 Register
**POST** `/api/auth/register`

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "role": "member"
}
```

**Password Requirements:**
- En az 8 karakter
- En az 1 büyük harf
- En az 1 küçük harf
- En az 1 rakam
- En az 1 özel karakter (!@#$%^&*...)

**Response:**
```json
{
  "success": true,
  "message": "Kayıt başarılı",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "role": "member"
  }
}
```

### 1.2 Login
**POST** `/api/auth/login`

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "SecurePass123!"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Giriş başarılı",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "role": "member"
  }
}
```

---

## 2. Book Endpoints

### 2.1 Get All Books (Paginated)
**GET** `/api/books?page=1&per_page=10`

**Query Parameters:**
- `page` (optional, default: 1)
- `per_page` (optional, default: 10, max: 100)

**Response:**
```json
{
  "success": true,
  "books": [...],
  "pagination": {
    "page": 1,
    "per_page": 10,
    "total": 45,
    "pages": 5,
    "has_next": true,
    "has_prev": false
  }
}
```

### 2.2 Get Available Books
**GET** `/api/books/available`

### 2.3 Get Book by ID
**GET** `/api/books/{book_id}`

### 2.4 Search Books
**GET** `/api/books/search?q=clean+code`

### 2.5 Create Book (Admin Only)
**POST** `/api/books`

**Request Body:**
```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "978-0132350884",
  "publisher": "Prentice Hall",
  "publication_year": 2008,
  "total_copies": 5
}
```

### 2.6 Update Book (Admin Only)
**PUT** `/api/books/{book_id}`

### 2.7 Delete Book (Admin Only)
**DELETE** `/api/books/{book_id}`

---

## 3. Borrowing Endpoints

### 3.1 Borrow Book
**POST** `/api/borrowings`

**Request Body:**
```json
{
  "book_id": 5,
  "days": 14
}
```

### 3.2 Return Book
**POST** `/api/borrowings/{borrowing_id}/return`

### 3.3 Get My Borrowings
**GET** `/api/borrowings/my`

### 3.4 Get All Borrowings (Admin Only)
**GET** `/api/borrowings`

### 3.5 Get Active Borrowings (Admin Only)
**GET** `/api/borrowings/active`

### 3.6 Get Borrowings Report (Admin Only)
**GET** `/api/borrowings/report?start_date=2024-01-01&end_date=2024-12-31`

---

## 4. Fine Endpoints

### 4.1 Get My Fines
**GET** `/api/fines/my`

### 4.2 Get My Unpaid Fines
**GET** `/api/fines/my/unpaid`

### 4.3 Pay Fine
**POST** `/api/fines/{fine_id}/pay`

### 4.4 Get All Fines (Admin Only)
**GET** `/api/fines`

### 4.5 Get All Unpaid Fines (Admin Only)
**GET** `/api/fines/unpaid`

---

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "error": "validation_error",
  "message": "Şifre en az 8 karakter olmalı"
}
```

### 401 Unauthorized
```json
{
  "success": false,
  "error": "authentication_error",
  "message": "Token gerekli"
}
```

### 403 Forbidden
```json
{
  "success": false,
  "error": "authorization_error",
  "message": "Admin yetkisi gerekli"
}
```

### 404 Not Found
```json
{
  "success": false,
  "error": "not_found",
  "message": "Kitap bulunamadı"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "error": "internal_server_error",
  "message": "Sunucu hatası oluştu"
}
```

---

## Rate Limiting
Şu anda rate limiting yok (eklenecek).

## Changelog
- **v1.0.0** - Initial API release
- **v1.1.0** - Pagination support added
- **v1.2.0** - Strong password policy implemented
