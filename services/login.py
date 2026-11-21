from fastapi import HTTPException 
from database.connect import koneksi
from services.security_hash import cek_hash
from services.token_services import buat_token

# fungsi yang digunakan untuk mengecek akun saat ingin login
def cek_akun(username, password):
    db = koneksi()
    cursor = db.cursor()
    
    try:
        cursor.execute(
        "SELECT id, password FROM users WHERE username = ? ",
        (username,)
        )
        pengecekan = cursor.fetchone()

        if pengecekan is None:
            raise HTTPException (status_code= 401, detail= 'username atau password anda salah')

        # fungsi yang digunakan unutk mengirim id agar dibuatkan token
        if cek_hash(password, pengecekan[1]):
            token = buat_token(pengecekan[0])
            return token
        ##############

        raise HTTPException(status_code= 401, detail= 'username atau password anda salah')

    finally:
        db.close()