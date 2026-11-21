from pydantic import BaseModel, field_validator
from datetime import date

class PenjualanInput(BaseModel):
    id_produk: int
    jumlah: int
    tanggal: str


    @field_validator('jumlah')
    @classmethod
    def cek_jumlah(cls, nilai):
        if nilai <= 0:
            raise ValueError('jumlah tidak boleh nol')
        return nilai

    @field_validator('tanggal')
    @classmethod
    def cek_tanggal(cls, nilai):
        try:
            date.fromisoformat(nilai)
        except ValueError:
            raise ValueError ('tanggal harus berupa yyyy-mm-dd, contoh 2026-11-19')
        return nilai