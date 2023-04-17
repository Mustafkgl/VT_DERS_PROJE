from werkzeug.security import generate_password_hash
import psycopg2
from datetime import datetime, timedelta
import random

# Veritabanı bağlantısı
conn = psycopg2.connect(
    dbname="library_db",
    user="library_user",
    password="library123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

print("📚 Veritabanı Doldurma Başladı...")

# 1. Kullanıcılar ekle
print("\n👤 Kullanıcılar ekleniyor...")
users = [
    ('ahmet_yilmaz', 'ahmet@email.com', 'member'),
    ('ayse_demir', 'ayse@email.com', 'member'),
    ('mehmet_kaya', 'mehmet@email.com', 'member'),
    ('fatma_celik', 'fatma@email.com', 'member'),
    ('mustafa_arslan', 'mustafa@email.com', 'member'),
    ('zeynep_ozturk', 'zeynep@email.com', 'member'),
    ('ali_yildiz', 'ali@email.com', 'member'),
    ('elif_sahin', 'elif@email.com', 'member'),
    ('can_kara', 'can@email.com', 'member'),
    ('selin_kurt', 'selin@email.com', 'member'),
]

for username, email, role in users:
    hashed_password = generate_password_hash('123456')
    try:
        cur.execute(
            "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
            (username, email, hashed_password, role)
        )
        print(f"  ✓ {username} eklendi")
    except Exception as e:
        print(f"  ✗ {username} eklenemedi: {e}")
        conn.rollback()
        continue

conn.commit()

# Kullanıcı ID'lerini al
cur.execute("SELECT id FROM users WHERE role = 'member'")
user_ids = [row[0] for row in cur.fetchall()]

# Kitap ID'lerini al
cur.execute("SELECT id FROM books")
book_ids = [row[0] for row in cur.fetchall()]

# 2. Ödünç alma kayıtları ekle
print("\n📖 Ödünç alma kayıtları oluşturuluyor...")

borrowings_data = []

# Aktif ödünç kayıtları (iade edilmemiş)
for _ in range(15):
    user_id = random.choice(user_ids)
    book_id = random.choice(book_ids)
    borrow_date = datetime.now() - timedelta(days=random.randint(1, 20))
    due_date = borrow_date + timedelta(days=14)

    borrowings_data.append((
        user_id, book_id, borrow_date, due_date, None, 'borrowed'
    ))

# İade edilmiş kayıtlar (zamanında)
for _ in range(25):
    user_id = random.choice(user_ids)
    book_id = random.choice(book_ids)
    borrow_date = datetime.now() - timedelta(days=random.randint(30, 90))
    due_date = borrow_date + timedelta(days=14)
    return_date = borrow_date + timedelta(days=random.randint(7, 13))  # Zamanında iade

    borrowings_data.append((
        user_id, book_id, borrow_date, due_date, return_date, 'returned'
    ))

# Gecikmeli iade edilmiş kayıtlar (ceza var)
for _ in range(10):
    user_id = random.choice(user_ids)
    book_id = random.choice(book_ids)
    borrow_date = datetime.now() - timedelta(days=random.randint(45, 120))
    due_date = borrow_date + timedelta(days=14)
    return_date = due_date + timedelta(days=random.randint(3, 15))  # Gecikmeli iade

    borrowings_data.append((
        user_id, book_id, borrow_date, due_date, return_date, 'overdue'
    ))

for i, (user_id, book_id, borrow_date, due_date, return_date, status) in enumerate(borrowings_data, 1):
    try:
        cur.execute(
            """INSERT INTO borrowings
               (user_id, book_id, borrow_date, due_date, return_date, status)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (user_id, book_id, borrow_date, due_date, return_date, status)
        )

        # Eğer gecikmeli iade varsa, trigger otomatik ceza oluşturacak
        if status == 'overdue' and return_date:
            # Trigger'ın çalışması için update yapalım
            cur.execute(
                "UPDATE borrowings SET return_date = %s WHERE id = (SELECT MAX(id) FROM borrowings)",
                (return_date,)
            )

        print(f"  ✓ Ödünç kaydı {i}/{len(borrowings_data)} - Durum: {status}")
    except Exception as e:
        print(f"  ✗ Ödünç kaydı {i} eklenemedi: {e}")
        conn.rollback()
        continue

conn.commit()

# 3. Kitap stoklarını güncelle (ödünç alınmış kitaplar için)
print("\n📦 Kitap stokları güncelleniyor...")
cur.execute("""
    UPDATE books
    SET available_copies = total_copies - (
        SELECT COUNT(*)
        FROM borrowings
        WHERE borrowings.book_id = books.id
        AND borrowings.status = 'borrowed'
    )
""")
conn.commit()

# 4. İstatistikler
print("\n" + "="*50)
print("📊 VERİTABANI İSTATİSTİKLERİ")
print("="*50)

cur.execute("SELECT COUNT(*) FROM users WHERE role = 'member'")
print(f"👥 Üye Sayısı: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM users WHERE role = 'admin'")
print(f"👨‍💼 Admin Sayısı: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM books")
print(f"📚 Toplam Kitap: {cur.fetchone()[0]}")

cur.execute("SELECT SUM(total_copies) FROM books")
print(f"📖 Toplam Kopya: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM borrowings")
print(f"📋 Toplam Ödünç Kaydı: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM borrowings WHERE status = 'borrowed'")
print(f"🔄 Aktif Ödünç: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM borrowings WHERE status = 'returned'")
print(f"✅ İade Edilmiş: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM borrowings WHERE status = 'overdue'")
print(f"⚠️  Gecikmeli İade: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM fines")
print(f"💰 Toplam Ceza Kaydı: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM fines WHERE paid = false")
print(f"❌ Ödenmemiş Ceza: {cur.fetchone()[0]}")

cur.execute("SELECT COALESCE(SUM(amount), 0) FROM fines WHERE paid = false")
print(f"💵 Toplam Borç: {cur.fetchone()[0]} TL")

print("="*50)
print("\n✨ Tüm veriler başarıyla eklendi!")
print("\n🔑 Test Kullanıcıları:")
print("   Admin: admin / admin123")
print("   Üye: ahmet_yilmaz / 123456")
print("   Üye: ayse_demir / 123456")
print("   (Tüm üyeler için şifre: 123456)")

cur.close()
conn.close()
