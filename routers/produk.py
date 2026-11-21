from fastapi import APIRouter, Depends
from models.produk import ProdukInput
from services.dependencies import user_saat_ini
from services.produk import tambah_produk, baca_produk, ubah_data_produk, hapus_produk

router = APIRouter(prefix='/produk', tags=['produk'])

@router.post('')
def tambah(data: ProdukInput, user_id: int = Depends(user_saat_ini)):
    return tambah_produk(user_id, data.nama_barang, data.harga, data.stok_barang)

@router.get('')
def lihat(user_id: int = Depends(user_saat_ini)):
    return baca_produk(user_id)

@router.put('/{id_produk}')
def ubah(id_produk: int, data: ProdukInput, user_id: int = Depends(user_saat_ini)):
    return ubah_data_produk(user_id, id_produk, data.nama_barang, data.harga, data.stok_barang)

@router.delete('/{id_produk}')
def hapus(id_produk: int, user_id: int = Depends(user_saat_ini)):
    return hapus_produk(user_id, id_produk)