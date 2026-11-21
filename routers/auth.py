from fastapi import APIRouter, Depends
from models.user import UserInput
from services.registrasi import buat_akun
from services.login import cek_akun
from services.dependencies import user_saat_ini

router = APIRouter()

@router.post('/registrasi')
def registrasi(user: UserInput):
    return buat_akun(user.username, user.password)

@router.post('/login')
def login(user: UserInput):
    return cek_akun(user.username, user.password)

@router.get('/me')
def me(user_id: int = Depends(user_saat_ini)):
    return {'user_id': user_id}