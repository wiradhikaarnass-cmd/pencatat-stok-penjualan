import os
import jwt
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

# fungsi yang digunakan untuk membuat token
load_dotenv()

SECRET = os.getenv('JWT_SECRET')
if not SECRET:
    raise RuntimeError('JWT_SECRET belum dibuat di file .env')

ALGORITHM = 'HS256'
EXP_TIME = 60

def buat_token(user_id):
    payload = {
        'sub': str(user_id),
        'exp': datetime.now(timezone.utc) + timedelta(minutes= EXP_TIME)
    }

    return jwt.encode(payload, SECRET, algorithm= ALGORITHM)

# ini akan di kirim ke fungsi depeden
def cek_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except jwt.InvalidTokenError:
        return None