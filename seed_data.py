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