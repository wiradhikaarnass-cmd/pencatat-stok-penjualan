from pydantic import BaseModel, field_validator

class ProdukInput(BaseModel):
    nama_barang: str
    harga: int
    stok_barang: int

    @field_validator('nama_barang')
    @classmethod
    def cek_nama_barang(cls, nilai):
        if not nilai.strip(): 
            raise ValueError('nama barang tidak boleh kosong')
        return nilai

    @field_validator('harga')
    @classmethod
    def cek_harga(cls, nilai):
        if nilai <= 0:
            raise ValueError('harga tidak boleh nol atau minus')
        return nilai
    
    @field_validator('stok_barang')
    @classmethod
    def cek_stok_barang(cls, nilai):
        if nilai < 0:
            raise ValueError('barang tidak boleh minus')
        return nilai

