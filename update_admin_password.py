from werkzeug.security import generate_password_hash
import psycopg2

# Veritabanı bağlantısı
conn = psycopg2.connect(
    dbname="library_db",
    user="library_user",