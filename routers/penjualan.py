from fastapi import APIRouter, Depends, Query
from models.penjualan import PenjualanInput
from services.dependencies import user_saat_ini
from services.penjualan import catat_penjualan, lihat_daftar_penjualan, laporan_penjualan

router = APIRouter(prefix='/penjualan', tags=['penjualan'])

@router.post('')
def tambah(data: PenjualanInput, user_id: int = Depends(user_saat_ini)):
    return catat_penjualan(user_id, data.id_produk, data.jumlah, data.tanggal)

@router.get('')
def lihat(tanggal: str | None = Query(default=None, pattern=r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'),
user_id: int = Depends(user_saat_ini)):
    return lihat_daftar_penjualan(user_id, tanggal)

@router.get('/laporan')
def total(tanggal: str = Query(pattern=r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'), 
user_id: int = Depends(user_saat_ini)):
    return laporan_penjualan(user_id, tanggal)