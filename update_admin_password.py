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
