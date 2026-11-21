import sqlite3
from fastapi import HTTPException
from database.connect import koneksi
from services.security_hash import buat_hash

# ini adalah fungsi yang digunakan ketika membuat akun
def buat_akun(username, password):
    db = koneksi()
    cursor = db.cursor()

    password_hash = buat_hash(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES(?, ?)",
            (username, password_hash.decode())
            )
        db.commit()
        return 'akun berhasil dibuat'
    
    except sqlite3.IntegrityError:
        raise HTTPException (status_code=409, detail='username atau password telah digunakan')

    finally:
        db.close()