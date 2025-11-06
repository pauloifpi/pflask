import sqlite3
import psycopg2
# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_8Hhg1vyBEkSo@ep-mute-mouse-ahmo4kka-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require"

def get_connection():
    conn = psycopg2.connect(DB_PATH)
    return conn
    