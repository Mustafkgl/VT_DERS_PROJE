# Akıllı Kütüphane Yönetim Sistemi


![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)
![Security](https://img.shields.io/badge/Security%20Score-92.50%2F100-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

**Modern, güvenli ve ölçeklenebilir kütüphane yönetim sistemi**

[Demo](#-demo) • [Özellikler](#-özellikler) • [Kurulum](#-kurulum) • [Kullanım](#-kullanım) • [API](#-api-dokümantasyonu) • [Güvenlik](#-güvenlik)

</div>

---

## İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Demo](#-demo)
- [Teknoloji Stack](#-teknoloji-stack)
- [Mimari](#-mimari)
- [Güvenlik](#-güvenlik)
- [Gereksinimler](#-gereksinimler)
- [Kurulum](#-kurulum)
  - [Windows Kurulumu](#windows-kurulumu)
  - [Linux Kurulumu](#linux-kurulumu)
  - [macOS Kurulumu](#macos-kurulumu)
  - [Docker Kurulumu](#docker-kurulumu)
- [Kullanım](#-kullanım)
- [Sayfa Detayları](#-sayfa-detayları)
- [API Dokümantasyonu](#-api-dokümantasyonu)
- [Veritabanı](#-veritabanı)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Geliştirme](#-geliştirme)
- [Katkıda Bulunma](#-katkıda-bulunma)

---

## Proje Hakkında

Akıllı Kütüphane Yönetim Sistemi, modern web teknolojileri kullanılarak geliştirilmiş, **güvenlik odaklı**, **ölçeklenebilir** ve **kullanıcı dostu** bir full-stack web uygulamasıdır.

### Proje Amacı

- Kütüphanelerin kitap envanteri, üye yönetimi ve ödünç işlemlerini dijitalleştirmek
- Modern güvenlik best practice'lerini uygulamak
- Katmanlı mimari ile sürdürülebilir kod yazmak
- PostgreSQL trigger ve stored procedure kullanımını öğretmek
- RESTful API tasarımını göstermek

### Hedef Kitle

- Küçük ve orta ölçekli kütüphaneler
- Eğitim kurumları (okul, üniversite kütüphaneleri)
- Yazılım öğrencileri (full-stack örnek proje)
- Flask ve PostgreSQL öğrenmek isteyenler

---

## Özellikler

### Güvenlik Özellikleri

- ✅ **SQL Injection Koruması** - SQLAlchemy ORM ile %100 korumalı
- ✅ **XSS Koruması** - Backend ve frontend HTML escaping
- ✅ **JWT Authentication** - Token tabanlı güvenli kimlik doğrulama
- ✅ **Şifre Hash'leme** - PBKDF2-SHA256 ile 600,000 iteration
- ✅ **Güçlü Şifre Politikası** - 8+ karakter, büyük/küçük harf, rakam, özel karakter, yaygın şifre blacklist
- ✅ **Role-Based Access Control** - Admin ve üye rolleri
- ✅ **Input Validation** - Kapsamlı girdi doğrulama
- ✅ **Atomic Transactions** - Race condition önleme, ACID uyumlu işlemler
- ✅ **Custom Error Handling** - Anlamlı hata mesajları, structured exception handling
- ✅ **Comprehensive Logging** - Structured JSON logging ile audit trail
- ✅ **Security Event Logging** - Ayrı güvenlik olayları log dosyası
- ✅ **CORS Configuration** - Güvenli origin kontrolü (.env yapılandırmalı)
- ✅ **Rate Limiting** - Brute force koruması (Flask-Limiter)
- ✅ **Security Headers** - XSS, clickjacking, MIME sniffing koruması
- ⚠️ **CSRF Protection** - Önerilen (eklenebilir)

### Kütüphane Özellikleri

#### Kitap Yönetimi
- Kitap ekleme, düzenleme, silme (Admin)
- Kitap arama (başlık, yazar)
- Stok takibi (toplam/mevcut kopya)
- ISBN validasyonu
- Yayın yılı kontrolü

#### Kullanıcı Yönetimi
- **Kullanıcı kayıt sayfası** - Yeni üyeler kendilerini kaydedebilir
- **Güçlü şifre politikası** - 8+ karakter, karmaşıklık gereksinimleri
- Güvenli giriş/çıkış
- JWT token bazlı oturum
- Rol bazlı yetkilendirme (Admin/Member)

#### Ödünç Alma Sistemi
- Kitap ödünç alma (14 gün)
- Kitap iade etme
- Aktif ödünç listesi
- Geçmiş ödünç kayıtları
- Due date (iade tarihi) takibi

#### Otomatik Ceza Sistemi
- PostgreSQL trigger ile otomatik hesaplama
- Günlük 2 TL ceza
- Gecikmeli iade tespiti
- Ceza ödeme sistemi
- Ödenmemiş ceza listesi

#### Raporlama (Admin)
- Tarih aralığına göre ödünç raporu
- Stored procedure ile optimize edilmiş sorgular
- Kullanıcı, kitap ve ceza bilgileri
- Detaylı istatistikler

### Kullanıcı Arayüzü

- Responsive tasarım (mobil uyumlu)
- Tab-based interface (Kitaplar, Ödünç, Cezalar, Admin)
- Real-time arama
- Dinamik içerik yükleme
- Kullanıcı dostu hata mesajları

### Kalite ve Test

- ✅ **Unit Tests** - pytest ile 17+ test case
- ✅ **Test Coverage** - %60-70 kod kapsama
- ✅ **Integration Tests** - API endpoint testleri
- ✅ **SQLite Test DB** - In-memory test database
- ✅ **CI/CD Ready** - pytest-cov ile raporlama

### Geliştirici Özellikleri

- ✅ **Type Hints** - Python type annotations (kritik modüller)
- ✅ **Database Migrations** - Flask-Migrate/Alembic entegrasyonu
- ✅ **API Pagination** - Performanslı veri listeleme
- ✅ **Custom Exceptions** - 8 özel exception class
- ✅ **Global Error Handlers** - Flask error handler middleware
- ✅ **API Documentation** - Detaylı endpoint dokümanları
- ✅ **Git Best Practices** - .gitignore ile güvenli versiyon kontrolü

---

## Demo

### Giriş Sayfası

```
┌─────────────────────────────────────────┐
│   Kütüphane Yönetim Sistemi             │
│                                         │
│   Kullanıcı Adı: [______________]       │
│   Şifre:         [______________]       │
│                                         │
│          [ Giriş Yap ]                  │
│                                         │
│   Varsayılan Admin: admin / admin123    │
└─────────────────────────────────────────┘
```

### Ana Dashboard (Kitaplar Sekmesi)

```
┌──────────────────────────────────────────────────────────────┐
│  Kütüphane Yönetim Sistemi          admin (Yönetici) [Çıkış] │
├──────────────────────────────────────────────────────────────┤
│ [Kitaplar] [Ödünç Kitaplarım] [Cezalar] [Admin Panel]        │
├──────────────────────────────────────────────────────────────┤
│  Kitap ara: [___________________] [Ara]                      │
│                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐          │
│  │ Clean Code           │  │ Design Patterns      │          │
│  │ Robert C. Martin     │  │ Gang of Four         │          │
│  │ ISBN: 978-0132...    │  │ ISBN: 978-0201...    │          │
│  │ Mevcut: 3 / 5        │  │ Mevcut: 0 / 2        │          │
│  │ [Ödünç Al]           │  │ Stokta yok           │          │
│  └──────────────────────┘  └──────────────────────┘          │
│                                                              │
│  ┌──────────────────────┐  ┌──────────────────────┐          │
│  │ Refactoring          │  │ The Pragmatic...     │          │
│  │ Martin Fowler        │  │ Andrew Hunt          │          │
│  │ ...                  │  │ ...                  │          │
│  └──────────────────────┘  └──────────────────────┘          │
└──────────────────────────────────────────────────────────────┘
```

### Admin Panel

```
┌─────────────────────────────────────────────────────────┐
│  Admin Panel                                            │
│                                                         │
│  ┌─ Yeni Kitap Ekle ────────────────────────────────┐   │
│  │  Başlık:      [_________________________]        │   │
│  │  Yazar:       [_________________________]        │   │
│  │  ISBN:        [_________________________]        │   │
│  │  Kopya Sayısı: [___]                             │   │
│  │                              [Kitap Ekle]        │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─ Rapor Al ───────────────────────────────────────┐   │
│  │  Başlangıç: [2025-01-01] Bitiş: [2025-12-31]     │   │
│  │                              [Rapor Getir]       │   │
│  │                                                  │   │
│  │  Rapor Sonuçları (45 kayıt)                      │   │
│  │  ┌────────────────────────────────────────────┐  │   │
│  │  │ Kullanıcı: ahmet_yilmaz                    │  │   │
│  │  │ Kitap: Clean Code - Robert C. Martin       │  │   │
│  │  │ Durum: İade Edildi                         │  │   │
│  │  │ Ceza: 0.00 TL                              │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## Teknoloji Stack

### Backend

| Teknoloji | Versiyon | Kullanım Amacı |
|-----------|----------|----------------|
| **Python** | 3.8+ | Ana programlama dili |
| **Flask** | 3.0.0 | Web framework |
| **Flask-SQLAlchemy** | 3.1.1 | ORM (Object-Relational Mapping) |
| **Flask-Migrate** | 4.0.5 | Database migrations (Alembic) |
| **Flask-CORS** | 4.0.0 | Cross-Origin Resource Sharing |
| **PostgreSQL** | 12+ | İlişkisel veritabanı |
| **psycopg2-binary** | Latest | PostgreSQL adaptörü |
| **PyJWT** | 2.8.0 | JWT token işlemleri |
| **Werkzeug** | 3.0.1 | Şifre hash'leme, güvenlik |
| **python-dotenv** | 1.0.0 | Environment variables |
| **pytest** | 7.4.3 | Unit testing framework |
| **pytest-flask** | 1.3.0 | Flask testing utilities |
| **pytest-cov** | 4.1.0 | Test coverage reporting |

### Frontend

| Teknoloji | Açıklama |
|-----------|----------|
| **Vanilla JavaScript** | Framework kullanmadan saf JS (ES6+) |
| **HTML5** | Semantic markup |
| **CSS3** | Flexbox, Grid, Responsive design |
| **Fetch API** | RESTful API çağrıları |
| **LocalStorage** | Token ve user bilgisi saklama |

### Veritabanı

| Özellik | Detay |
|---------|-------|
| **DBMS** | PostgreSQL 12+ |
| **ORM** | SQLAlchemy |
| **Migrations** | Flask-Migrate (Alembic) |
| **Triggers** | 1 adet (otomatik ceza hesaplama) |
| **Stored Procedures** | 1 adet (raporlama) |
| **Indexes** | 9 adet (performans) |

### DevOps & Tools

- **Git** - Version control
- **pip** - Python package manager
- **Virtual Environment** - Dependency isolation
- **Docker** - Containerization (opsiyonel)
- **Nginx** - Reverse proxy (production)
- **Gunicorn** - WSGI server (production)

---

## Mimari

### Katmanlı Mimari (Layered Architecture)

```
┌───────────────────────────────────────────────────────┐
│                   PRESENTATION LAYER                  │
│              (Controllers - API Endpoints)            │
│                                                       │
│  auth_controller.py  book_controller.py               │
│  borrowing_controller.py  fine_controller.py          │
│  middleware.py (JWT validation)                       │
└─────────────────────┬─────────────────────────────────┘
                      │
┌─────────────────────▼─────────────────────────────────┐
│                 BUSINESS LOGIC LAYER                  │
│                     (Services)                        │
│                                                       │
│  auth_service.py     book_service.py                  │
│  borrowing_service.py fine_service.py                 │
│  - Input validation                                   │
│  - Business rules                                     │
│  - Data transformation                                │
└─────────────────────┬─────────────────────────────────┘
                      │
┌─────────────────────▼─────────────────────────────────┐
│                  DATA ACCESS LAYER                    │
│                   (Repositories)                      │
│                                                       │
│  user_repository.py   book_repository.py              │
│  borrowing_repository.py fine_repository.py           │
│  - CRUD operations                                    │
│  - ORM queries                                        │
│  - Transaction management                             │
└─────────────────────┬─────────────────────────────────┘
                      │
┌─────────────────────▼─────────────────────────────────┐
│                    DATABASE LAYER                     │
│                    (PostgreSQL)                       │
│                                                       │
│  Tables: users, books, borrowings, fines              │
│  Triggers: calculate_fine_on_return                   │
│  Stored Procedures: get_borrowings_report             │
│  Constraints: FK, Check, Unique                       │
└───────────────────────────────────────────────────────┘
```

### Proje Dizin Yapısı

```
kutuphane_projesi/
│
├── app/                          # Ana uygulama paketi
│   ├── __init__.py              # Flask app factory
│   │
│   ├── controllers/             # API endpoint'leri (Controller Layer)
│   │   ├── __init__.py
│   │   ├── auth_controller.py   # /api/auth/* endpoints
│   │   ├── book_controller.py   # /api/books/* endpoints
│   │   ├── borrowing_controller.py  # /api/borrowings/* endpoints
│   │   ├── fine_controller.py   # /api/fines/* endpoints
│   │   └── middleware.py        # @token_required, @admin_required
│   │
│   ├── services/                # İş mantığı (Business Logic Layer)
│   │   ├── __init__.py
│   │   ├── auth_service.py      # Login, register, JWT
│   │   ├── book_service.py      # Kitap CRUD, validation
│   │   ├── borrowing_service.py # Ödünç/iade mantığı
│   │   └── fine_service.py      # Ceza hesaplama, ödeme
│   │
│   ├── repositories/            # Veritabanı erişimi (Data Access Layer)
│   │   ├── __init__.py
│   │   ├── user_repository.py   # User CRUD
│   │   ├── book_repository.py   # Book CRUD, search
│   │   ├── borrowing_repository.py  # Borrowing CRUD, report
│   │   └── fine_repository.py   # Fine CRUD
│   │
│   ├── models/                  # SQLAlchemy ORM modelleri
│   │   ├── __init__.py
│   │   ├── user.py              # User entity
│   │   ├── book.py              # Book entity
│   │   ├── borrowing.py         # Borrowing entity
│   │   └── fine.py              # Fine entity
│   │
│   └── utils/                   # Yardımcı araçlar
│       ├── __init__.py
│       ├── validators.py        # Input validation, sanitization
│       ├── logger.py            # Structured JSON logging sistemi
│       └── security_logger.py   # Güvenlik olayları logging
│
├── logs/                        # Log dosyaları (auto-generated)
│   ├── app.log                 # Genel uygulama logları
│   ├── error.log               # Sadece ERROR+ logları
│   └── security.log            # Güvenlik olayları
│
├── templates/                   # HTML şablonları
│   ├── index.html              # Login sayfası
│   ├── register.html           # Kullanıcı kayıt sayfası
│   └── dashboard.html          # Ana dashboard
│
├── static/                      # Statik dosyalar
│   ├── app.js                  # Frontend JavaScript (278 satır)
│   └── style.css               # CSS stilleri (224 satır)
│
├── venv/                        # Python virtual environment
│
├── config.py                    # Uygulama yapılandırması
├── run.py                       # Uygulama başlatıcı
├── requirements.txt             # Python bağımlılıkları
├── .env                         # Ortam değişkenleri (SECRET!)
├── .env.example                 # Ortam değişkenleri şablonu
│
├── schema.sql                   # Veritabanı şeması (DDL)
├── seed_data.py                 # Test verisi oluşturucu (Python)
├── seed_data.sql                # Kitap test verileri (SQL)
├── users_seed.sql               # Kullanıcı verileri (SQL)
├── update_admin_password.py     # Admin şifre hash'leme
│
├── PROJE_RAPORU.md             # Detaylı proje dokümantasyonu
├── GUVENLIK_RAPORU.md          # Güvenlik analizi (temel)
├── GUVENLIK_RAPORU_DETAYLI.md  # Detaylı güvenlik raporu
└── README.md                    # Bu dosya
```

### Request Flow Örneği

**Senaryo:** Kullanıcı kitap ödünç alıyor

```
1. Frontend (app.js)
   └─> fetch('/api/borrowings', {method: 'POST', body: {book_id: 5}})

2. Controller (borrowing_controller.py)
   └─> @token_required decorator
       └─> Token doğrulama (middleware.py)
           └─> JWT decode, user_id al

3. Service (borrowing_service.py)
   └─> borrow_book(user_id, book_id)
       ├─> Kullanıcı var mı? (UserRepository)
       ├─> Kitap var mı? (BookRepository)
       ├─> Stok var mı? (book.available_copies > 0)
       ├─> Due date hesapla (14 gün sonra)
       └─> Borrowing oluştur (BorrowingRepository)
           └─> Stok güncelle (available_copies - 1)

4. Repository (borrowing_repository.py)
   └─> Borrowing.create(user_id, book_id, due_date)
       └─> SQLAlchemy ORM
           └─> INSERT INTO borrowings ...

5. Database (PostgreSQL)
   └─> Transaction commit
       └─> Return borrowing record

6. Response
   └─> JSON: {'success': True, 'borrowing': {...}}
       └─> Frontend: Alert "Kitap ödünç alındı!"
```

---

## Güvenlik

### Uygulanan Güvenlik Önlemleri

#### 1. SQL Injection Koruması ✅ %100 Güvenli

**Yöntem:** SQLAlchemy ORM kullanımı

```python
# ✅ GÜVENLİ - Parametreli sorgu
books = Book.query.filter(
    Book.title.ilike(f'%{user_input}%')
).all()

# SQLAlchemy oluşturur:
# SELECT * FROM books WHERE title ILIKE %s
# Parameters: ['%user_input%']
```

**Neden Güvenli:**
- Kullanıcı girdisi direkt SQL'e eklenmez
- ORM otomatik parametrelendirme yapar
- PostgreSQL prepared statements kullanır

#### 2. XSS (Cross-Site Scripting) Koruması ✅ İyi

**Backend Sanitization:**
```python
from html import escape

def sanitize_text(text):
    return escape(str(text).strip())

# Kullanım
title = sanitize_text("<script>alert('XSS')</script>")
# Sonuç: "&lt;script&gt;alert('XSS')&lt;/script&gt;"
```

**Frontend Escaping:**
```javascript
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Kullanım
innerHTML = `<h4>${escapeHtml(book.title)}</h4>`;
```

#### 3. Authentication (JWT) ✅ Güvenli

**Token Yapısı:**
```json
{
  "user_id": 1,
  "username": "admin",
  "role": "admin",
  "exp": 1735258000
}
```

**Özellikler:**
- ✅ HS256 algoritması
- ✅ 24 saat expiration
- ✅ Signature validation
- ✅ Algorithm whitelist

#### 4. Authorization (RBAC) ✅ Güvenli

**Rol Bazlı Erişim Kontrolü:**

| İşlem | Admin | Member |
|-------|-------|--------|
| Kitap görüntüleme | ✅ | ✅ |
| Kitap ekleme/silme | ✅ | ❌ |
| Kitap ödünç alma | ✅ | ✅ |
| Rapor görüntüleme | ✅ | ❌ |
| Tüm ödünç kayıtları | ✅ | ❌ (sadece kendi) |

#### 5. Şifre Güvenliği ✅ Yüksek

**Hash Algoritması:** PBKDF2-SHA256

```python
# Kayıt
user.password = generate_password_hash('admin123')
# Sonuç: pbkdf2:sha256:600000$abc123$def456...

# Doğrulama
is_valid = check_password_hash(user.password, 'admin123')
```

**Özellikler:**
- 600,000 iterations (brute force'a karşı)
- Unique salt (her şifre için)
- Constant-time comparison (timing attack koruması)

#### 6. Input Validation ✅ Kapsamlı

**Doğrulanan Alanlar:**

| Alan | Validation | Örnek |
|------|------------|-------|
| **Email** | Regex | `user@example.com` |
| **Username** | 3-50 karakter, alfanumerik | `john_doe` |
| **ISBN** | 10 veya 13 haneli | `978-3-16-148410-0` |
| **Year** | 1000-2100 arası | `2023` |
| **Password** | Min 6 karakter | `admin123` |

#### 7. Logging ve Audit Trail ✅ Kapsamlı

**Structured JSON Logging:**

Uygulama, tüm önemli olayları JSON formatında loglar. Her log kaydı:
- Timestamp (UTC)
- Log seviyesi (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Module ve fonksiyon bilgisi
- Request context (IP, user agent, method, path)
- Extra data (işleme özel bilgiler)
- Exception tracking (hata durumlarında)

**Log Dosyaları:**

| Dosya | İçerik | Rotasyon | Retention |
|-------|--------|----------|-----------|
| `logs/app.log` | Genel uygulama logları | 10 MB | 10 dosya |
| `logs/error.log` | Sadece ERROR+ seviyesi | 10 MB | 10 dosya |
| `logs/security.log` | Güvenlik olayları | 10 MB | 20 dosya |

**Security Event Logging:**

Ayrı bir güvenlik logger'ı şu olayları kaydeder:

```python
# Login denemesi
security_logger.log_login_attempt(
    username='admin',
    success=True,
    user_id=1
)

# Yetkisiz erişim
security_logger.log_unauthorized_access(
    endpoint='/api/admin/users',
    user_id=5,
    required_role='admin'
)

# Token validasyon
security_logger.log_token_validation(
    success=False,
    reason='Token expired'
)

# Admin işlemleri
security_logger.log_admin_action(
    admin_id=1,
    action='delete_book',
    target_type='book',
    target_id=42
)

# Veri erişimi (Audit Trail)
security_logger.log_data_access(
    user_id=5,
    resource_type='borrowing',
    resource_id=123,
    action='create'
)

# Validation hataları
security_logger.log_validation_error(
    field='isbn',
    value='invalid',
    error_type='Invalid ISBN format'
)
```

**Loglanan Güvenlik Olayları:**

- ✅ **Login/Logout** - Başarılı ve başarısız girişler
- ✅ **Registration** - Yeni kullanıcı kayıtları
- ✅ **Token Events** - Token oluşturma, validasyon, expiration
- ✅ **Unauthorized Access** - Yetkisiz erişim denemeleri
- ✅ **Admin Actions** - Tüm admin işlemleri (CRUD)
- ✅ **Data Access** - Kritik veri erişimleri (audit trail)
- ✅ **Validation Errors** - Input validation hataları
- ✅ **Password Changes** - Şifre değişiklikleri
- ✅ **Suspicious Activity** - Anormal davranışlar
- ✅ **Rate Limit Events** - Rate limit aşımları (hazır)

**Log Örneği (JSON Format):**

```json
{
  "timestamp": "2024-01-15T10:30:45.123456",
  "level": "WARNING",
  "logger": "security",
  "message": "Failed login attempt: admin - Invalid password",
  "module": "auth_service",
  "function": "login",
  "line": 82,
  "request": {
    "method": "POST",
    "path": "/api/auth/login",
    "ip": "192.168.1.100",
    "user_agent": "Mozilla/5.0..."
  },
  "extra": {
    "event": "login_attempt",
    "username": "admin",
    "success": false,
    "reason": "Invalid password"
  }
}
```

**Avantajlar:**
- 📊 **Analiz:** JSON format ile kolay analiz (ELK Stack, Splunk)
- 🔍 **Sorun Tespiti:** Detaylı hata tracking
- 🛡️ **Güvenlik:** Saldırı tespiti ve forensics
- 📈 **Monitoring:** Performans ve kullanım metrikleri
- ✅ **Compliance:** Audit trail gereksinimleri

### Uygulanan Yeni Güvenlik Önlemleri ✅

#### 9. Rate Limiting ✅ Uygulandı

**Kütüphane:** Flask-Limiter

```python
# Login endpoint - 5 deneme/dakika
@limiter.limit("5 per minute")
def login():
    ...

# Register endpoint - 3 kayıt/saat
@limiter.limit("3 per hour")
def register():
    ...
```

**Limitler:**
- **Login:** 5 başarısız deneme/dakika (brute force koruması)
- **Register:** 3 kayıt/saat (spam koruması)
- **Genel API:** 200 istek/dakika
- **Admin API:** 50 istek/dakika

**Avantajlar:**
- ✅ Brute force saldırı koruması
- ✅ DDoS hafifletme
- ✅ API abuse önleme

#### 10. Security Headers ✅ Uygulandı

**Eklenen HTTP Güvenlik Başlıkları:**

```python
# XSS Koruması
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block

# Clickjacking Koruması
X-Frame-Options: DENY

# HTTPS Zorunluluğu
Strict-Transport-Security: max-age=31536000; includeSubDomains

# Content Security Policy
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; ...

# Privacy
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=(), camera=()
```

**Korunan Saldırılar:**
- ✅ Clickjacking
- ✅ MIME type sniffing
- ✅ XSS (katmanlı koruma)
- ✅ Man-in-the-middle (HTTPS zorunlu)

#### 11. Güvenli CORS Yapılandırması ✅

**Önceki:** `origins: "*"` ❌ (Tüm domainlere açık - tehlikeli!)

**Şimdi:**
```python
CORS_ORIGINS=http://localhost:3000,http://localhost:5000
```

**.env.example Dosyası:**
Hassas bilgiler artık .env.example'da şablon olarak saklanıyor.

### Bilinen Güvenlik Eksiklikleri

| Eksik | Risk Seviyesi | Açıklama |
|-------|---------------|----------|
| **Account Lockout** | 🟡 Orta | Çok fazla başarısız deneme sonrası hesap kilidi yok |
| **CSRF Protection** | 🟡 Orta | Token kullanımı riski azaltır |
| **Token Revocation** | 🟡 Orta | Logout sonrası token geçerli kalıyor |
| **2FA/MFA** | 🟢 Düşük | İki faktörlü doğrulama yok (opsiyonel) |


## 📋 Gereksinimler

### Sistem Gereksinimleri

| Bileşen | Minimum | Önerilen |
|---------|---------|----------|
| **İşletim Sistemi** | Windows 10 / Linux / macOS 10.14+ | - |
| **RAM** | 2 GB | 4 GB+ |
| **Disk Alanı** | 500 MB | 1 GB+ |
| **Python** | 3.8 | 3.10+ |
| **PostgreSQL** | 12 | 14+ |

### Yazılım Gereksinimleri

- **Python 3.8+** ([İndir](https://www.python.org/downloads/))
- **PostgreSQL 12+** ([İndir](https://www.postgresql.org/download/))
- **pip** (Python ile birlikte gelir)
- **Git** (opsiyonel) ([İndir](https://git-scm.com/downloads))

---

## Kurulum

### Windows Kurulumu

#### Adım 1: Python Kurulumu

1. [Python'ı indirin](https://www.python.org/downloads/) (3.8 veya üzeri)
2. Kurulum sırasında **"Add Python to PATH"** seçeneğini işaretleyin
3. Kurulumu doğrulayın:

```cmd
python --version
# Çıktı: Python 3.10.x
```

#### Adım 2: PostgreSQL Kurulumu

1. [PostgreSQL'i indirin](https://www.postgresql.org/download/windows/)
2. Kurulum sırasında şifre belirleyin (örn: `postgres`)
3. Port: `5432` (varsayılan)
4. Kurulumu doğrulayın:

```cmd
psql --version
# Çıktı: psql (PostgreSQL) 14.x
```

#### Adım 3: Projeyi İndirin

**Git ile:**
```cmd
git clone <repository-url>
cd kutuphane_projesi
```

**Veya ZIP olarak indirip açın**

#### Adım 4: Virtual Environment Oluşturun

```cmd
# Virtual environment oluştur
python -m venv venv

# Aktifleştir
venv\Scripts\activate

# Aktif olduğunu doğrulayın (prompt başında (venv) görünmeli)
```

#### Adım 5: Bağımlılıkları Yükleyin

```cmd
pip install -r requirements.txt
```

#### Adım 6: PostgreSQL Veritabanı Oluşturun

```cmd
# PostgreSQL'e bağlan
psql -U postgres

# SQL komutları (psql içinde)
CREATE DATABASE library_db;
CREATE USER library_user WITH PASSWORD 'library123';
GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
\q

# Şemayı ve verileri yükle
psql -U library_user -d library_db -f schema.sql
psql -U library_user -d library_db -f users_seed.sql
psql -U library_user -d library_db -f seed_data.sql
```

#### Adım 7: Ortam Değişkenlerini Ayarlayın

`.env.example` dosyasını `.env` olarak kopyalayın ve düzenleyin:

```cmd
copy .env.example .env
```

`.env` dosyasını düzenleyin:

```env
SECRET_KEY=your-secret-key-here-change-in-production
DB_USER=library_user
DB_PASSWORD=library123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=library_db
CORS_ORIGINS=http://localhost:3000,http://localhost:5000
FLASK_ENV=development
```

#### Adım 8: Bağımlılıkları Yükleyin

Yeni güvenlik kütüphaneleri eklendiği için:

```cmd
pip install -r requirements.txt
```

#### Adım 9: Test Verisi Yükleyin (Opsiyonel)

```cmd
python seed_data.py
```

#### Adım 10: Uygulamayı Başlatın

```cmd
python run.py
```

Tarayıcınızda açın: **http://localhost:5000**

#### Adım 11: Giriş Yapın

- **Admin:** `admin` / `admin123`
- **Üye:** `ahmet_yilmaz` / `123456`

---

### Linux Kurulumu

#### Ubuntu/Debian

```bash
# Sistem paketlerini güncelle
sudo apt update && sudo apt upgrade -y

# Python ve pip yükle
sudo apt install python3 python3-pip python3-venv -y

# PostgreSQL yükle
sudo apt install postgresql postgresql-contrib -y

# PostgreSQL servisini başlat
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Proje dizinine git
cd /home/yourusername

# Projeyi klon
git clone <repository-url>
cd kutuphane_projesi

# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Bağımlılıklar
pip install -r requirements.txt

# PostgreSQL veritabanı
sudo -u postgres psql <<EOF
CREATE DATABASE library_db;
CREATE USER library_user WITH PASSWORD 'library123';
GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
\q
EOF

# Ortam değişkenleri ayarla
cp .env.example .env
# .env dosyasını düzenleyin

# Şema ve verileri yükle
psql -U library_user -d library_db -f schema.sql
psql -U library_user -d library_db -f users_seed.sql
psql -U library_user -d library_db -f seed_data.sql

# Test verisi (opsiyonel - Python ile)
# python seed_data.py

# Başlat
python run.py
```

#### CentOS/RHEL/Fedora

```bash
# Python yükle
sudo dnf install python3 python3-pip -y

# PostgreSQL yükle
sudo dnf install postgresql-server postgresql-contrib -y

# PostgreSQL initialize
sudo postgresql-setup --initdb

# Servisi başlat
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Geri kalan adımlar Ubuntu ile aynı
```

---

### macOS Kurulumu

#### Adım 1: Homebrew Yükleyin (yoksa)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Adım 2: Python ve PostgreSQL Yükleyin

```bash
# Python yükle
brew install python3

# PostgreSQL yükle
brew install postgresql@14

# PostgreSQL başlat
brew services start postgresql@14

# Kurulumları doğrula
python3 --version
psql --version
```

#### Adım 3: Projeyi Kurun

```bash
# Proje dizinine git
cd ~/Documents

# Projeyi klon
git clone <repository-url>
cd kutuphane_projesi

# Virtual environment
python3 -m venv venv
source venv/bin/activate

# Bağımlılıklar
pip install -r requirements.txt

# PostgreSQL veritabanı
psql postgres <<EOF
CREATE DATABASE library_db;
CREATE USER library_user WITH PASSWORD 'library123';
GRANT ALL PRIVILEGES ON DATABASE library_db TO library_user;
\q
EOF

# Ortam değişkenleri
cp .env.example .env
# .env dosyasını düzenleyin

# Şema ve verileri yükle
psql -U library_user -d library_db -f schema.sql
psql -U library_user -d library_db -f users_seed.sql
psql -U library_user -d library_db -f seed_data.sql

# Başlat
python run.py
```

---

### Docker Kurulumu

#### Dockerfile

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Bağımlılıklar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyaları
COPY . .

# Port
EXPOSE 5000

# Başlat
CMD ["python", "run.py"]
```

#### docker-compose.yml

```yaml
version: '3.8'

services:
  db:
    image: postgres:14
    environment:
      POSTGRES_DB: library_db
      POSTGRES_USER: library_user
      POSTGRES_PASSWORD: library123
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./schema.sql:/docker-entrypoint-initdb.d/schema.sql

  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      DB_HOST: db
      DB_PORT: 5432
      DB_NAME: library_db
      DB_USER: library_user
      DB_PASSWORD: library123
      SECRET_KEY: your-secret-key-here
    volumes:
      - .:/app

volumes:
  postgres_data:
```

#### Çalıştırma

```bash
# Build ve başlat
docker-compose up --build

# Arka planda çalıştır
docker-compose up -d

# Logları görüntüle
docker-compose logs -f

# Durdur
docker-compose down
```

---

## 💻 Kullanım

### Temel Kullanım Akışı

#### 1. Yeni Üye Kaydı

```
1. http://localhost:5000 adresine gidin
2. "Hesabınız yok mu? Kayıt Ol" linkine tıklayın
3. Kayıt formunu doldurun:
   - Kullanıcı Adı (3-50 karakter, sadece harf, rakam, _, -)
   - E-posta
   - Şifre (en az 8 karakter, büyük/küçük harf, rakam, özel karakter)
   - Şifre Tekrar
4. "Kayıt Ol" butonuna tıklayın
5. Başarılı kayıt sonrası login sayfasına yönlendirilirsiniz
```

**Şifre Gereksinimleri:**
- ✅ En az 8 karakter
- ✅ En az 1 büyük harf (A-Z)
- ✅ En az 1 küçük harf (a-z)
- ✅ En az 1 rakam (0-9)
- ✅ En az 1 özel karakter (!@#$%^&*...)

**Güvenlik:** Rate limiting aktif - 3 kayıt/saat

#### 2. Giriş Yapma

```
1. http://localhost:5000 adresine gidin
2. Kullanıcı adı ve şifre girin
3. "Giriş Yap" butonuna tıklayın
4. Başarılı girişte dashboard'a yönlendirilirsiniz
```

**Test Kullanıcıları:**
- **Admin:** `admin` / `admin123`
- **Üye:** `ahmet_yilmaz` / `123456`
- **Üye:** `ayse_demir` / `123456`

**Güvenlik:** Rate limiting aktif - 5 deneme/dakika

#### 3. Kitap Arama

```
1. "Kitaplar" sekmesine gidin
2. Arama kutusuna kitap adı veya yazar adı girin
3. "Ara" butonuna tıklayın
4. Sonuçlar dinamik olarak gösterilir
```

#### 4. Kitap Ödünç Alma

```
1. Mevcut bir kitabın "Ödünç Al" butonuna tıklayın
2. Onay mesajı görünür: "Kitap ödünç alındı!"
3. "Ödünç Kitaplarım" sekmesinde görünür
4. İade tarihi: Ödünç alma tarihinden 14 gün sonra
```

#### 5. Kitap İade Etme

```
1. "Ödünç Kitaplarım" sekmesine gidin
2. İade edilecek kitabın "İade Et" butonuna tıklayın
3. Onay mesajı: "Kitap iade edildi!"
4. Eğer gecikme varsa, otomatik ceza oluşturulur
```

#### 6. Ceza Ödeme

```
1. "Cezalar" sekmesine gidin
2. Ödenmemiş cezalar listelenir
3. Toplam borç gösterilir
4. Her cezanın "Öde" butonuna tıklayarak ödeme yapabilirsiniz
```

#### 7. Kitap Ekleme (Admin)

```
1. "Admin Panel" sekmesine gidin (sadece admin görebilir)
2. "Yeni Kitap Ekle" formunu doldurun:
   - Başlık
   - Yazar
   - ISBN (opsiyonel)
   - Kopya Sayısı
3. "Kitap Ekle" butonuna tıklayın
4. Başarı mesajı: "Kitap eklendi!"
```

#### 7. Rapor Alma (Admin)

```
1. "Admin Panel" sekmesinde "Rapor Al" bölümüne gidin
2. Başlangıç ve bitiş tarihlerini seçin
3. "Rapor Getir" butonuna tıklayın
4. Detaylı rapor gösterilir:
   - Kullanıcı bilgileri
   - Kitap bilgileri
   - Ödünç durumu
   - Ceza bilgileri
```

### API Kullanımı (cURL Örnekleri)

#### Login

```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'

# Response:
# {
#   "success": true,
#   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#   "user": {"id": 1, "username": "admin", "role": "admin"}
# }
```

#### Kitap Listesi

```bash
TOKEN="your-jwt-token-here"

curl http://localhost:5000/api/books \
  -H "Authorization: Bearer $TOKEN"
```

#### Kitap Ödünç Alma

```bash
curl -X POST http://localhost:5000/api/borrowings \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"book_id":5,"days":14}'
```

---

## Sayfa Detayları

### 1. Login Sayfası (`index.html`)

**URL:** `http://localhost:5000/`

**Parametreler:**

| Alan | Input Name | Type | Validation | Açıklama |
|------|------------|------|------------|----------|
| Kullanıcı Adı | `username` | text | Required | 3-50 karakter |
| Şifre | `password` | password | Required | Min 6 karakter |

**İşlem Akışı:**
```
1. Form submit → preventDefault()
2. Değerleri al: username, password
3. POST /api/auth/login
4. Success → Token ve user bilgisi localStorage'a kaydet
5. Redirect → /dashboard
6. Fail → Hata mesajı göster
```

**JavaScript Fonksiyonu:**
```javascript
// static/app.js (login sayfası script bölümü)
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password})
    });

    const data = await response.json();
    if (data.success) {
        localStorage.setItem('token', data.token);
        localStorage.setItem('user', JSON.stringify(data.user));
        window.location.href = '/dashboard';
    } else {
        messageDiv.textContent = data.message;
    }
});
```

**Kontrol Edilen Parametreler:**
- ✅ Boş alan kontrolü (frontend)
- ✅ Kullanıcı adı/şifre doğrulaması (backend)
- ✅ Rate limiting yok (eklenebilir)

---

### 2. Dashboard Sayfası (`dashboard.html`)

**URL:** `http://localhost:5000/dashboard`

**Sekmeler:**
1. **Kitaplar** (Tüm kullanıcılar)
2. **Ödünç Kitaplarım** (Tüm kullanıcılar)
3. **Cezalar** (Tüm kullanıcılar)
4. **Admin Panel** (Sadece admin)

---

#### 2.1 Kitaplar Sekmesi

**JavaScript Fonksiyon:** `loadBooks()`

**API Endpoint:** `GET /api/books`

**Kontrol Edilen Parametreler:**

| Parametre | Kaynak | Kontrol | Açıklama |
|-----------|--------|---------|----------|
| `token` | localStorage | JWT validation | Kimlik doğrulama |
| `book.title` | API response | XSS escape | `escapeHtml()` ile temizlenir |
| `book.author` | API response | XSS escape | `escapeHtml()` ile temizlenir |
| `book.isbn` | API response | XSS escape | `escapeHtml()` ile temizlenir |
| `book.available_copies` | API response | Number | Stok kontrolü |

**Arama Fonksiyonu:** `searchBooks()`

```javascript
async function searchBooks() {
    const query = document.getElementById('searchInput').value;

    if (!query) {
        loadBooks();  // Boşsa tüm kitapları göster
        return;
    }

    const data = await apiCall(`/api/books/search?q=${query}`);
    // Sonuçları render et
}
```

**Kontrol:**
- ✅ `query` parametresi backend'de SQL Injection'a karşı korumalı (ORM)
- ✅ XSS escape (frontend)

**Ödünç Al Butonu:**

```javascript
async function borrowBook(bookId) {
    const data = await apiCall('/api/borrowings', 'POST', {book_id: bookId});

    if (data.success) {
        alert('Kitap ödünç alındı!');
        loadBooks();  // Listeyi güncelle
    } else {
        alert(data.message);
    }
}
```

**Kontrol Edilen Parametreler (Backend):**
- ✅ `book_id`: Integer validation
- ✅ `user_id`: JWT token'dan alınır (güvenilir)
- ✅ Stok kontrolü: `book.available_copies > 0`
- ✅ Kitap var mı kontrolü

---

#### 2.2 Ödünç Kitaplarım Sekmesi

**JavaScript Fonksiyon:** `loadMyBorrowings()`

**API Endpoint:** `GET /api/borrowings/my`

**Kontrol Edilen Parametreler:**

| Parametre | Kaynak | Kontrol | Açıklama |
|-----------|--------|---------|----------|
| `user_id` | JWT token | Automatic | Middleware'den gelir |
| `borrowing.book_id` | Database | - | Foreign key |
| `borrowing.borrow_date` | Database | Date format | ISO 8601 |
| `borrowing.due_date` | Database | Date format | ISO 8601 |
| `borrowing.return_date` | Database | Date format | Nullable |
| `borrowing.status` | Database | Enum check | borrowed/returned/overdue |

**İade Et Butonu:**

```javascript
async function returnBook(borrowingId) {
    const data = await apiCall(`/api/borrowings/${borrowingId}/return`, 'POST');

    if (data.success) {
        alert('Kitap iade edildi!');
        loadMyBorrowings();
        loadMyFines();  // Ceza oluşmuş olabilir
    }
}
```

**Backend Kontrolü (borrowing_service.py):**
```python
def return_book(borrowing_id):
    borrowing = BorrowingRepository.find_by_id(borrowing_id)

    # Kontroller:
    # 1. Borrowing var mı?
    if not borrowing:
        return {'success': False, 'message': 'Kayıt bulunamadı'}

    # 2. Zaten iade edilmiş mi?
    if borrowing.status != 'borrowed':
        return {'success': False, 'message': 'Zaten iade edilmiş'}

    # 3. İade yap (trigger devreye girer)
    returned = BorrowingRepository.return_book(borrowing_id)

    # 4. Stok güncelle
    BookRepository.increase_available_copies(borrowing.book_id)

    return {'success': True, 'borrowing': returned.to_dict()}
```

**PostgreSQL Trigger (Otomatik Ceza Hesaplama):**

```sql
-- Trigger fonksiyonu (schema.sql:61-104)
CREATE OR REPLACE FUNCTION calculate_fine_on_return()
RETURNS TRIGGER AS $$
DECLARE
    days_late INTEGER;
    fine_amount DECIMAL(10, 2);
BEGIN
    -- return_date set edildiğinde
    IF NEW.return_date IS NOT NULL AND OLD.return_date IS NULL THEN

        -- Gecikme hesapla
        days_late := EXTRACT(DAY FROM (NEW.return_date - NEW.due_date));

        IF days_late > 0 THEN
            -- Günlük 2 TL ceza
            fine_amount := days_late * 2.00;

            -- Durumu 'overdue' yap
            NEW.status := 'overdue';

            -- Ceza kaydı oluştur
            INSERT INTO fines (borrowing_id, user_id, amount, paid)
            VALUES (NEW.id, NEW.user_id, fine_amount, FALSE);
        ELSE
            -- Zamanında iade
            NEW.status := 'returned';
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

**Kontrol Edilen Parametreler (Trigger):**
- ✅ `return_date`: Timestamp
- ✅ `due_date`: Timestamp
- ✅ Gecikme günü: `EXTRACT(DAY FROM ...)`
- ✅ Ceza tutarı: `days_late * 2.00`

---

#### 2.3 Cezalar Sekmesi

**JavaScript Fonksiyon:** `loadMyFines()`

**API Endpoint:** `GET /api/fines/my/unpaid`

**Kontrol Edilen Parametreler:**

| Parametre | Kaynak | Kontrol | Açıklama |
|-----------|--------|---------|----------|
| `user_id` | JWT token | Automatic | Middleware |
| `fine.amount` | Database | Decimal(10,2) | Para formatı |
| `fine.paid` | Database | Boolean | Ödeme durumu |
| `total_amount` | Backend | SUM() | Toplam borç |

**Ceza Öde Butonu:**

```javascript
async function payFine(fineId) {
    const data = await apiCall(`/api/fines/${fineId}/pay`, 'POST');

    if (data.success) {
        alert('Ceza ödendi!');
        loadMyFines();
    }
}
```

**Backend (fine_service.py):**

```python
def pay_fine(fine_id):
    # Cezayı bul
    fine = FineRepository.mark_as_paid(fine_id)

    if fine:
        return {'success': True, 'message': 'Ceza ödendi', 'fine': fine.to_dict()}

    return {'success': False, 'message': 'Ceza bulunamadı'}
```

**Kontrol:**
- ✅ `fine_id`: Integer, exists check
- ✅ `paid`: Boolean update (False → True)

---

#### 2.4 Admin Panel Sekmesi

**Görünürlük:** `if (user.role === 'admin')`

**2 ana bölüm:**

##### A. Yeni Kitap Ekle

**Form Parametreleri:**

| Alan | Input ID | Type | Validation (Frontend) | Validation (Backend) |
|------|----------|------|----------------------|----------------------|
| Başlık | `bookTitle` | text | Required | sanitize_text, max 200 |
| Yazar | `bookAuthor` | text | Required | sanitize_text, max 100 |
| ISBN | `bookISBN` | text | Optional | validate_isbn (10/13 digit) |
| Kopya Sayısı | `bookCopies` | number | Min 1 | validate_positive_integer (1-1000) |

**JavaScript (Form Submit):**

```javascript
document.getElementById('addBookForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const bookData = {
        title: document.getElementById('bookTitle').value,
        author: document.getElementById('bookAuthor').value,
        isbn: document.getElementById('bookISBN').value,
        total_copies: parseInt(document.getElementById('bookCopies').value)
    };

    const data = await apiCall('/api/books', 'POST', bookData);

    if (data.success) {
        alert('Kitap eklendi!');
        document.getElementById('addBookForm').reset();
        loadBooks();
    } else {
        alert(data.message);
    }
});
```

**Backend Validation (book_service.py:8-51):**

```python
def create_book(title, author, isbn=None, publisher=None, publication_year=None, total_copies=1):
    # 1. Required field check
    if not title or not author:
        return {'success': False, 'message': 'Başlık ve yazar gerekli'}

    # 2. XSS sanitization
    title = InputValidator.sanitize_text(title, max_length=200)
    author = InputValidator.sanitize_text(author, max_length=100)

    # 3. ISBN validation
    if isbn and not InputValidator.validate_isbn(isbn):
        return {'success': False, 'message': 'Geçersiz ISBN'}

    # 4. Year validation
    if publication_year and not InputValidator.validate_year(publication_year):
        return {'success': False, 'message': 'Geçersiz yıl'}

    # 5. Copy count validation
    if not InputValidator.validate_positive_integer(total_copies, 1, 1000):
        return {'success': False, 'message': 'Geçersiz kopya sayısı (1-1000)'}

    # 6. Create book
    book = BookRepository.create(title, author, isbn, publisher, publication_year, total_copies, total_copies)

    if book:
        return {'success': True, 'message': 'Kitap eklendi', 'book': book.to_dict()}

    return {'success': False, 'message': 'Kitap eklenemedi'}
```

**Kontrol Edilen Her Şey:**
- ✅ XSS: HTML escape
- ✅ SQL Injection: ORM
- ✅ ISBN format: Regex
- ✅ Year range: 1000-2100
- ✅ Copies range: 1-1000
- ✅ Max length: title 200, author 100

---

##### B. Rapor Al

**Form Parametreleri:**

| Alan | Input ID | Type | Format | Backend Validation |
|------|----------|------|--------|-------------------|
| Başlangıç Tarihi | `reportStartDate` | date | YYYY-MM-DD | datetime.fromisoformat() |
| Bitiş Tarihi | `reportEndDate` | date | YYYY-MM-DD | datetime.fromisoformat() |

**JavaScript:**

```javascript
async function getReport() {
    const startDate = document.getElementById('reportStartDate').value;
    const endDate = document.getElementById('reportEndDate').value;

    // Validation
    if (!startDate || !endDate) {
        alert('Lütfen tarih aralığı seçin');
        return;
    }

    // API çağrısı
    const data = await apiCall(
        `/api/borrowings/report?start_date=${startDate}&end_date=${endDate}`
    );

    if (data.success) {
        // Raporu render et (XSS escape ile)
        reportResult.innerHTML = `
            <h4>Rapor Sonuçları (${data.report.length} kayıt)</h4>
            ${data.report.map(r => `
                <div class="item-card">
                    <p><strong>Kullanıcı:</strong> ${escapeHtml(r.user_name)}</p>
                    <p><strong>Kitap:</strong> ${escapeHtml(r.book_title)}</p>
                    <p><strong>Durum:</strong> ${getStatusTurkce(r.status)}</p>
                    <p><strong>Ceza:</strong> ${r.fine_amount} TL</p>
                </div>
            `).join('')}
        `;
    }
}
```

**Backend (borrowing_controller.py:56-76):**

```python
@borrowing_bp.route('/report', methods=['GET'])
@admin_required
def get_borrowings_report(current_user):
    # Query parameters
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    # Validation
    if not all([start_date_str, end_date_str]):
        return jsonify({'success': False, 'message': 'Tarih gerekli'}), 400

    try:
        start_date = datetime.fromisoformat(start_date_str)
        end_date = datetime.fromisoformat(end_date_str)
    except ValueError:
        return jsonify({'success': False, 'message': 'Geçersiz tarih'}), 400

    # Stored procedure çağrısı
    result = BorrowingService.get_borrowings_report(start_date, end_date)

    if result['success']:
        return jsonify(result), 200
    return jsonify(result), 400
```

**PostgreSQL Stored Procedure (schema.sql:117-156):**

```sql
CREATE OR REPLACE FUNCTION get_borrowings_report(
    start_date TIMESTAMP,
    end_date TIMESTAMP
)
RETURNS TABLE (
    borrowing_id INTEGER,
    user_name VARCHAR(80),
    user_email VARCHAR(120),
    book_title VARCHAR(200),
    book_author VARCHAR(100),
    borrow_date TIMESTAMP,
    due_date TIMESTAMP,
    return_date TIMESTAMP,
    status VARCHAR(20),
    fine_amount DECIMAL(10, 2),
    fine_paid BOOLEAN
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        b.id AS borrowing_id,
        u.username AS user_name,
        u.email AS user_email,
        bk.title AS book_title,
        bk.author AS book_author,
        b.borrow_date,
        b.due_date,
        b.return_date,
        b.status,
        COALESCE(f.amount, 0.00) AS fine_amount,
        COALESCE(f.paid, FALSE) AS fine_paid
    FROM borrowings b
    INNER JOIN users u ON b.user_id = u.id
    INNER JOIN books bk ON b.book_id = bk.id
    LEFT JOIN fines f ON b.id = f.borrowing_id
    WHERE b.borrow_date >= start_date
      AND b.borrow_date <= end_date
    ORDER BY b.borrow_date DESC;
END;
$$ LANGUAGE plpgsql;
```

**Kontrol Edilen Parametreler:**
- ✅ `start_date`: Timestamp validation, SQL parametreli
- ✅ `end_date`: Timestamp validation, SQL parametreli
- ✅ Date range: start <= end (frontend mantığı)
- ✅ SQL Injection: Named parameters (`:start_date`, `:end_date`)
- ✅ XSS: Frontend'de `escapeHtml()`

**Rapor Çıktısı Alanları:**
1. `borrowing_id` - Ödünç kayıt ID
2. `user_name` - Kullanıcı adı
3. `user_email` - Email
4. `book_title` - Kitap başlığı
5. `book_author` - Yazar
6. `borrow_date` - Ödünç alma tarihi
7. `due_date` - İade tarihi
8. `return_date` - Gerçek iade tarihi
9. `status` - Durum (borrowed/returned/overdue)
10. `fine_amount` - Ceza tutarı
11. `fine_paid` - Ceza ödenmiş mi

---

## 📡 API Dokümantasyonu

### Base URL

```
http://localhost:5000/api
```

### Authentication

Tüm korumalı endpoint'ler **JWT token** gerektirir.

**Header:**
```
Authorization: Bearer <your-jwt-token>
```

---

### Endpoint'ler

#### 1. Authentication

##### POST `/auth/register`

Yeni kullanıcı kaydı.

**Request:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure123",
  "role": "member"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Kayıt başarılı",
  "user": {
    "id": 10,
    "username": "john_doe",
    "email": "john@example.com",
    "role": "member",
    "created_at": "2025-12-26T10:00:00"
  }
}
```

**Validations:**
- `username`: 3-50 karakter, alfanumerik + `_-`
- `email`: RFC 5322 format
- `password`: Min 6 karakter
- `role`: `admin` veya `member`

---

##### POST `/auth/login`

Kullanıcı girişi.

**Request:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Giriş başarılı",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@library.com",
    "role": "admin",
    "created_at": "2025-01-01T00:00:00"
  }
}
```

**Response (401):**
```json
{
  "success": false,
  "message": "Kullanıcı adı veya şifre hatalı"
}
```

---

##### POST `/auth/verify`

Token doğrulama.

**Request:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response (200):**
```json
{
  "success": true,
  "payload": {
    "user_id": 1,
    "username": "admin",
    "role": "admin",
    "exp": 1735258000
  }
}
```

---

#### 2. Books

##### GET `/books`

Tüm kitapları listele. **(Token gerekli)**

**Response (200):**
```json
{
  "success": true,
  "books": [
    {
      "id": 1,
      "title": "Clean Code",
      "author": "Robert C. Martin",
      "isbn": "978-0132350884",
      "publisher": "Prentice Hall",
      "publication_year": 2008,
      "total_copies": 5,
      "available_copies": 3,
      "created_at": "2025-01-01T00:00:00"
    },
    ...
  ]
}
```

---

##### GET `/books/available`

Mevcut kitapları listele (`available_copies > 0`). **(Token gerekli)**

---

##### GET `/books/{id}`

Kitap detayı. **(Token gerekli)**

**Response (200):**
```json
{
  "success": true,
  "book": {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    ...
  }
}
```

**Response (404):**
```json
{
  "success": false,
  "message": "Kitap bulunamadı"
}
```

---

##### GET `/books/search?q=<query>`

Kitap ara (başlık veya yazar). **(Token gerekli)**

**Example:**
```
GET /api/books/search?q=clean
```

**Response (200):**
```json
{
  "success": true,
  "books": [
    {
      "id": 1,
      "title": "Clean Code",
      "author": "Robert C. Martin",
      ...
    }
  ]
}
```

**Validation:**
- `q`: SQL Injection korumalı (ORM)

---

##### POST `/books`

Yeni kitap ekle. **(Admin gerekli)**

**Request:**
```json
{
  "title": "Design Patterns",
  "author": "Gang of Four",
  "isbn": "978-0201633610",
  "publisher": "Addison-Wesley",
  "publication_year": 1994,
  "total_copies": 3
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Kitap eklendi",
  "book": {
    "id": 15,
    "title": "Design Patterns",
    ...
  }
}
```

**Validations:**
- `title`: Required, max 200 karakter, HTML escape
- `author`: Required, max 100 karakter, HTML escape
- `isbn`: Opsiyonel, 10 veya 13 haneli
- `publication_year`: 1000-2100 arası
- `total_copies`: 1-1000 arası

---

##### PUT `/books/{id}`

Kitap güncelle. **(Admin gerekli)**

**Request:**
```json
{
  "title": "Updated Title",
  "total_copies": 10
}
```

---

##### DELETE `/books/{id}`

Kitap sil. **(Admin gerekli)**

**Response (200):**
```json
{
  "success": true,
  "message": "Kitap silindi"
}
```

---

#### 3. Borrowings

##### POST `/borrowings`

Kitap ödünç al. **(Token gerekli)**

**Request:**
```json
{
  "book_id": 5,
  "days": 14
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Kitap ödünç alındı",
  "borrowing": {
    "id": 42,
    "user_id": 3,
    "book_id": 5,
    "borrow_date": "2025-12-26T10:00:00",
    "due_date": "2026-01-09T10:00:00",
    "return_date": null,
    "status": "borrowed",
    "created_at": "2025-12-26T10:00:00"
  }
}
```

**Response (400):**
```json
{
  "success": false,
  "message": "Kitap stokta yok"
}
```

**Validations:**
- `book_id`: Integer, exists check
- `days`: Integer, default 14
- Stok kontrolü: `available_copies > 0`

---

##### POST `/borrowings/{id}/return`

Kitap iade et. **(Token gerekli)**

**Response (200):**
```json
{
  "success": true,
  "message": "Kitap iade edildi",
  "borrowing": {
    "id": 42,
    "return_date": "2026-01-05T15:30:00",
    "status": "returned"
  }
}
```

**Trigger Etkisi:**
- Eğer gecikmeli iade: `status = 'overdue'`, `fines` tablosuna kayıt
- Zamanında iade: `status = 'returned'`

---

##### GET `/borrowings/my`

Kendi ödünç kayıtlarım. **(Token gerekli)**

**Response (200):**
```json
{
  "success": true,
  "borrowings": [
    {
      "id": 42,
      "book_id": 5,
      "borrow_date": "2025-12-26T10:00:00",
      "due_date": "2026-01-09T10:00:00",
      "return_date": null,
      "status": "borrowed"
    }
  ]
}
```

---

##### GET `/borrowings`

Tüm ödünç kayıtları. **(Admin gerekli)**

---

##### GET `/borrowings/active`

Aktif ödünç kayıtları (`status = 'borrowed'`). **(Admin gerekli)**

---

##### GET `/borrowings/report?start_date={start}&end_date={end}`

Tarih aralığına göre rapor (Stored Procedure). **(Admin gerekli)**

**Example:**
```
GET /api/borrowings/report?start_date=2025-01-01&end_date=2025-12-31
```

**Response (200):**
```json
{
  "success": true,
  "report": [
    {
      "borrowing_id": 42,
      "user_name": "ahmet_yilmaz",
      "user_email": "ahmet@email.com",
      "book_title": "Clean Code",
      "book_author": "Robert C. Martin",
      "borrow_date": "2025-12-01T10:00:00",
      "due_date": "2025-12-15T10:00:00",
      "return_date": "2025-12-20T15:30:00",
      "status": "overdue",
      "fine_amount": 10.00,
      "fine_paid": false
    }
  ]
}
```

---

#### 4. Fines

##### GET `/fines/my`

Tüm cezalarım. **(Token gerekli)**

---

##### GET `/fines/my/unpaid`

Ödenmemiş cezalarım. **(Token gerekli)**

**Response (200):**
```json
{
  "success": true,
  "fines": [
    {
      "id": 10,
      "borrowing_id": 42,
      "user_id": 3,
      "amount": 10.00,
      "paid": false,
      "created_at": "2025-12-20T15:30:00"
    }
  ],
  "total_amount": 10.00
}
```

---

##### POST `/fines/{id}/pay`

Ceza öde. **(Token gerekli)**

**Response (200):**
```json
{
  "success": true,
  "message": "Ceza ödendi",
  "fine": {
    "id": 10,
    "paid": true
  }
}
```

---

##### GET `/fines`

Tüm cezalar. **(Admin gerekli)**

---

##### GET `/fines/unpaid`

Tüm ödenmemiş cezalar. **(Admin gerekli)**

---

### HTTP Status Codes

| Code | Anlamı | Kullanım |
|------|--------|----------|
| **200** | OK | Başarılı GET, PUT, DELETE |
| **201** | Created | Başarılı POST (kayıt oluşturma) |
| **400** | Bad Request | Validation hatası, eksik parametre |
| **401** | Unauthorized | Token yok veya geçersiz |
| **403** | Forbidden | Yetkisiz erişim (admin gerekli) |
| **404** | Not Found | Kaynak bulunamadı |
| **500** | Internal Server Error | Sunucu hatası |

---

## Veritabanı

### Şema Diyagramı

```
┌─────────────────┐         ┌─────────────────┐
│     users       │         │     books       │
├─────────────────┤         ├─────────────────┤
│ id (PK)         │         │ id (PK)         │
│ username        │         │ title           │
│ password (hash) │         │ author          │
│ email           │         │ isbn            │
│ role            │         │ publisher       │
│ created_at      │         │ publication_year│
└────────┬────────┘         │ total_copies    │
         │                  │ available_copies│
         │                  └────────┬────────┘
         │                           │
         │    ┌──────────────────────┘
         │    │
         ▼    ▼
┌─────────────────────┐
│    borrowings       │
├─────────────────────┤
│ id (PK)             │
│ user_id (FK)        │◄─────┐
│ book_id (FK)        │      │
│ borrow_date         │      │
│ due_date            │      │
│ return_date         │      │
│ status              │      │
│ created_at          │      │
└──────────┬──────────┘      │
           │                 │
           ▼                 │
    ┌─────────────┐          │
    │    fines    │          │
    ├─────────────┤          │
    │ id (PK)     │          │
    │ borrowing_id│──────────┘
    │ user_id (FK)│
    │ amount      │
    │ paid        │
    │ created_at  │
    └─────────────┘
```

### Tablolar

#### 1. users

| Sütun | Tip | Kısıtlamalar | Açıklama |
|-------|-----|--------------|----------|
| `id` | SERIAL | PRIMARY KEY | Otomatik artan ID |
| `username` | VARCHAR(80) | UNIQUE, NOT NULL | Kullanıcı adı |
| `password` | VARCHAR(255) | NOT NULL | Hash'lenmiş şifre |
| `email` | VARCHAR(120) | UNIQUE, NOT NULL | Email adresi |
| `role` | VARCHAR(20) | NOT NULL, CHECK | admin/member |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Kayıt tarihi |

**Constraints:**
```sql
CHECK (role IN ('admin', 'member'))
```

---

#### 2. books

| Sütun | Tip | Kısıtlamalar | Açıklama |
|-------|-----|--------------|----------|
| `id` | SERIAL | PRIMARY KEY | Kitap ID |
| `title` | VARCHAR(200) | NOT NULL | Başlık |
| `author` | VARCHAR(100) | NOT NULL | Yazar |
| `isbn` | VARCHAR(20) | UNIQUE | ISBN numarası |
| `publisher` | VARCHAR(100) | - | Yayınevi |
| `publication_year` | INTEGER | - | Yayın yılı |
| `total_copies` | INTEGER | NOT NULL, DEFAULT 1 | Toplam kopya |
| `available_copies` | INTEGER | NOT NULL, DEFAULT 1 | Mevcut kopya |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Eklenme tarihi |

**Constraints:**
```sql
CHECK (available_copies >= 0 AND available_copies <= total_copies)
```

---

#### 3. borrowings

| Sütun | Tip | Kısıtlamalar | Açıklama |
|-------|-----|--------------|----------|
| `id` | SERIAL | PRIMARY KEY | Ödünç ID |
| `user_id` | INTEGER | FK → users(id) | Kullanıcı |
| `book_id` | INTEGER | FK → books(id) | Kitap |
| `borrow_date` | TIMESTAMP | DEFAULT NOW() | Ödünç tarihi |
| `due_date` | TIMESTAMP | NOT NULL | İade tarihi |
| `return_date` | TIMESTAMP | NULL | Gerçek iade |
| `status` | VARCHAR(20) | NOT NULL, CHECK | Durum |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Kayıt tarihi |

**Constraints:**
```sql
CHECK (status IN ('borrowed', 'returned', 'overdue'))
FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
```

**Indexes:**
```sql
CREATE INDEX idx_borrowings_user_id ON borrowings(user_id);
CREATE INDEX idx_borrowings_book_id ON borrowings(book_id);
CREATE INDEX idx_borrowings_status ON borrowings(status);
```

---

#### 4. fines

| Sütun | Tip | Kısıtlamalar | Açıklama |
|-------|-----|--------------|----------|
| `id` | SERIAL | PRIMARY KEY | Ceza ID |
| `borrowing_id` | INTEGER | FK → borrowings(id) | Ödünç kaydı |
| `user_id` | INTEGER | FK → users(id) | Kullanıcı |
| `amount` | DECIMAL(10,2) | NOT NULL, DEFAULT 0 | Tutar |
| `paid` | BOOLEAN | DEFAULT FALSE | Ödenmiş mi |
| `created_at` | TIMESTAMP | DEFAULT NOW() | Oluşturma |

**Indexes:**
```sql
CREATE INDEX idx_fines_user_id ON fines(user_id);
CREATE INDEX idx_fines_paid ON fines(paid);
```

---

### Triggers

#### calculate_fine_on_return

**Tetiklenme:** `BEFORE UPDATE ON borrowings`

**Amaç:** Kitap iade edildiğinde otomatik ceza hesaplama

**Mantık:**
```
1. return_date set edildiğinde tetiklenir
2. Gecikme hesapla: return_date - due_date
3. Eğer gecikme > 0:
   - Ceza tutarı = gecikme_günü * 2.00 TL
   - status = 'overdue'
   - fines tablosuna INSERT
4. Değilse:
   - status = 'returned'
```

**Örnek:**
```
Ödünç: 2025-12-01
Due date: 2025-12-15 (14 gün sonra)
İade: 2025-12-20 (5 gün gecikme)

Ceza = 5 * 2.00 = 10.00 TL
Status = 'overdue'
```

---

### Stored Procedures

#### get_borrowings_report(start_date, end_date)

**Amaç:** Tarih aralığına göre detaylı ödünç raporu

**Parametreler:**
- `start_date` (TIMESTAMP): Başlangıç tarihi
- `end_date` (TIMESTAMP): Bitiş tarihi

**Dönen Sütunlar:**
1. `borrowing_id` - Ödünç ID
2. `user_name` - Kullanıcı adı
3. `user_email` - Email
4. `book_title` - Kitap başlığı
5. `book_author` - Yazar
6. `borrow_date` - Ödünç alma
7. `due_date` - İade tarihi
8. `return_date` - Gerçek iade
9. `status` - Durum
10. `fine_amount` - Ceza
11. `fine_paid` - Ödendi mi

**Kullanım:**
```sql
SELECT * FROM get_borrowings_report('2025-01-01', '2025-12-31');
```

---

## Testing

### Manuel Test

#### 1. Giriş Testi

```bash
# Login request
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'

# Beklenen: 200 OK, token döner
```

#### 2. SQL Injection Testi

```bash
# Saldırı girişimi
curl "http://localhost:5000/api/books/search?q=' OR '1'='1" \
  -H "Authorization: Bearer <token>"

# Beklenen: Normal sonuç, injection çalışmaz
```

#### 3. XSS Testi

```bash
# Kötü niyetli kitap ekleme
curl -X POST http://localhost:5000/api/books \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"<script>alert(1)</script>","author":"Test"}'

# Veritabanında kontrol:
psql -U library_user -d library_db -c \
  "SELECT title FROM books WHERE author='Test';"

# Beklenen: &lt;script&gt;alert(1)&lt;/script&gt; (escaped)
```

#### 4. Authorization Testi

```bash
# Member olarak admin endpoint'e erişim
curl -X POST http://localhost:5000/api/books \
  -H "Authorization: Bearer <member_token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","author":"Test"}'

# Beklenen: 403 Forbidden
```

**Çalıştırma:**
```bash
python -m unittest discover tests/
```

---

## 🚢 Deployment

### Production Hazırlığı

#### 1. Güvenlik Yapılandırması

```python
# config.py (Production)
import os

class ProductionConfig:
    DEBUG = False
    TESTING = False

    # Güçlü secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Vault'tan al
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY must be set!")

    # Database (SSL ile)
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}'
        f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}'
        f'/{os.getenv("DB_NAME")}?sslmode=require'
    )

    # Security headers
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
```

#### 2. Gunicorn Kurulumu

```bash
# requirements.txt'e ekle
gunicorn==21.2.0

# Çalıştır
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

#### 3. Nginx Reverse Proxy

```nginx
# /etc/nginx/sites-available/library
server {
    listen 80;
    server_name yourdomain.com;

    # HTTPS'e yönlendir
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    # SSL sertifikaları (Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    # Security headers
    add_header X-Frame-Options "DENY";
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000";

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /var/www/library/static;
        expires 30d;
    }
}
```

#### 4. Systemd Service

```ini
# /etc/systemd/system/library.service
[Unit]
Description=Library Management System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/library
Environment="PATH=/var/www/library/venv/bin"
ExecStart=/var/www/library/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 run:app

[Install]
WantedBy=multi-user.target
```

**Başlatma:**
```bash
sudo systemctl enable library
sudo systemctl start library
sudo systemctl status library
```

#### 5. Let's Encrypt SSL

```bash
# Certbot yükle
sudo apt install certbot python3-certbot-nginx

# Sertifika al
sudo certbot --nginx -d yourdomain.com

# Otomatik yenileme
sudo systemctl enable certbot.timer
```

---

## Geliştirme

### Geliştirme Ortamı

```bash
# Virtual environment aktif
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Debug mode ile çalıştır
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows

python run.py
```

### Yeni Özellik Ekleme

#### Örnek: Kitap Favorileme

**1. Model ekle:**

```python
# app/models/favorite.py
from app.models.user import db
from datetime import datetime

class Favorite(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # İlişkiler
    user = db.relationship('User', backref='favorites')
    book = db.relationship('Book', backref='favorites')
```

**2. Repository ekle:**

```python
# app/repositories/favorite_repository.py
from app.models import db, Favorite

class FavoriteRepository:
    @staticmethod
    def add_favorite(user_id, book_id):
        try:
            favorite = Favorite(user_id=user_id, book_id=book_id)
            db.session.add(favorite)
            db.session.commit()
            return favorite
        except:
            db.session.rollback()
            return None
```

**3. Service ekle:**

```python
# app/services/favorite_service.py
from app.repositories.favorite_repository import FavoriteRepository

class FavoriteService:
    @staticmethod
    def add_favorite(user_id, book_id):
        favorite = FavoriteRepository.add_favorite(user_id, book_id)
        if favorite:
            return {'success': True, 'favorite': favorite.to_dict()}
        return {'success': False, 'message': 'Zaten favori'}
```

**4. Controller ekle:**

```python
# app/controllers/favorite_controller.py
from flask import Blueprint, jsonify, request
from app.services.favorite_service import FavoriteService
from app.controllers.middleware import token_required

favorite_bp = Blueprint('favorite', __name__, url_prefix='/api/favorites')

@favorite_bp.route('', methods=['POST'])
@token_required
def add_favorite(current_user):
    data = request.get_json()
    book_id = data.get('book_id')

    result = FavoriteService.add_favorite(current_user['user_id'], book_id)
    return jsonify(result), 201 if result['success'] else 400
```

**5. Blueprint kaydet:**

```python
# app/__init__.py
from app.controllers.favorite_controller import favorite_bp

app.register_blueprint(favorite_bp)
```

---

## 🙏 Teşekkürler

- [Flask](https://flask.palletsprojects.com/) - Awesome web framework
- [PostgreSQL](https://www.postgresql.org/) - Powerful database
- [SQLAlchemy](https://www.sqlalchemy.org/) - Great ORM
- [OWASP](https://owasp.org/) - Security guidelines

---

### Faydalı Linkler

- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [REST API Best Practices](https://restfulapi.net/)

---
