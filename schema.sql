-- Akıllı Kütüphane Yönetim Sistemi - Veritabanı Şeması

-- Kullanıcılar Tablosu
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('admin', 'member')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Kitaplar Tablosu
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    publisher VARCHAR(100),
    publication_year INTEGER,
    total_copies INTEGER NOT NULL DEFAULT 1,
    available_copies INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_copies CHECK (available_copies >= 0 AND available_copies <= total_copies)
);

-- Ödünç Alma İşlemleri Tablosu
CREATE TABLE IF NOT EXISTS borrowings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    book_id INTEGER NOT NULL REFERENCES books(id) ON DELETE CASCADE,
    borrow_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    due_date TIMESTAMP NOT NULL,
    return_date TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'borrowed' CHECK (status IN ('borrowed', 'returned', 'overdue')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cezalar Tablosu
CREATE TABLE IF NOT EXISTS fines (
    id SERIAL PRIMARY KEY,
    borrowing_id INTEGER NOT NULL REFERENCES borrowings(id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    paid BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- İndeksler (Performans için)
CREATE INDEX IF NOT EXISTS idx_borrowings_user_id ON borrowings(user_id);
CREATE INDEX IF NOT EXISTS idx_borrowings_book_id ON borrowings(book_id);
CREATE INDEX IF NOT EXISTS idx_borrowings_status ON borrowings(status);
CREATE INDEX IF NOT EXISTS idx_fines_user_id ON fines(user_id);
CREATE INDEX IF NOT EXISTS idx_fines_paid ON fines(paid);

-- =====================================================
-- TRIGGER: Kitap İade Edildiğinde Otomatik Ceza Hesaplama
-- =====================================================

-- Trigger Fonksiyonu
CREATE OR REPLACE FUNCTION calculate_fine_on_return()
RETURNS TRIGGER AS $$
DECLARE
    days_late INTEGER;
    fine_amount DECIMAL(10, 2);
    existing_fine_id INTEGER;
BEGIN
    -- Eğer return_date set edildiyse ve daha önce yoksa
    IF NEW.return_date IS NOT NULL AND OLD.return_date IS NULL THEN

        -- Gecikme gün sayısını hesapla
        days_late := EXTRACT(DAY FROM (NEW.return_date - NEW.due_date));

        -- Eğer gecikmeli iade varsa
        IF days_late > 0 THEN
            -- Günlük 2 TL ceza (örnek)
            fine_amount := days_late * 2.00;

            -- Durumu overdue yap
            NEW.status := 'overdue';

            -- Bu borrowing için daha önce ceza var mı kontrol et
            SELECT id INTO existing_fine_id
            FROM fines
            WHERE borrowing_id = NEW.id;

            -- Eğer ceza yoksa oluştur, varsa güncelle
            IF existing_fine_id IS NULL THEN
                INSERT INTO fines (borrowing_id, user_id, amount, paid)
                VALUES (NEW.id, NEW.user_id, fine_amount, FALSE);
            ELSE
                UPDATE fines
                SET amount = fine_amount
                WHERE id = existing_fine_id;
            END IF;
        ELSE
            -- Gecikmesiz iade
            NEW.status := 'returned';
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger Tanımı
DROP TRIGGER IF EXISTS trigger_calculate_fine ON borrowings;
CREATE TRIGGER trigger_calculate_fine
BEFORE UPDATE ON borrowings
FOR EACH ROW
EXECUTE FUNCTION calculate_fine_on_return();

-- =====================================================
-- STORED PROCEDURE: İki Tarih Arasındaki Ödünç Raporlama
-- =====================================================

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

-- =====================================================
-- Varsayılan Veriler (Admin Kullanıcı)
-- =====================================================

-- Admin kullanıcısı ekle (Şifre: admin123 - hash'lenecek)
INSERT INTO users (username, password, email, role)
VALUES ('admin', 'admin123', 'admin@library.com', 'admin')
ON CONFLICT (username) DO NOTHING;

-- Test için örnek kitap
INSERT INTO books (title, author, isbn, publisher, publication_year, total_copies, available_copies)
VALUES
    ('Python ile Programlama', 'Ahmet Yılmaz', '978-1234567890', 'Kodlama Yayınları', 2023, 5, 5),
    ('Veritabanı Yönetimi', 'Mehmet Demir', '978-0987654321', 'Teknoloji Kitapları', 2022, 3, 3)
ON CONFLICT (isbn) DO NOTHING;

-- Şema oluşturma tamamlandı
