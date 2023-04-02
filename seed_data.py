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