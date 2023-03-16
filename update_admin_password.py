from werkzeug.security import generate_password_hash
import psycopg2

# Veritabanı bağlantısı
conn = psycopg2.connect(
    dbname="library_db",
    user="library_user",
    password="library123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Admin şifresini hash'le
hashed_password = generate_password_hash('admin123')

# Veritabanını güncelle
cur.execute(
    "UPDATE users SET password = %s WHERE username = %s",
    (hashed_password, 'admin')
)

conn.commit()
cur.close()
conn.close()

print("Admin şifresi başarıyla hash'lendi!")
