import sqlite3
from fastapi import HTTPException
from database.connect import koneksi

def catat_penjualan(user_id, id_produk, jumlah, tanggal):
    db = koneksi()
    cursor = db.cursor()

    try:
        cursor.execute(
            "SELECT nama_barang, harga, stok_barang FROM produk WHERE id = ? AND user_id = ?",
            (id_produk, user_id)
        )
        data = cursor.fetchone()
        
        if data is None:
            raise HTTPException(status_code=404, detail='data produk tidak ditemukan')

        nama_barang, harga, stok_barang = data  # karna data ini menampung 3 list berbeda, kita masukan saja di masing" variabel
        
        if stok_barang < jumlah:
            raise HTTPException(status_code=400, detail='stok barang tidak cukup')
        
        total = harga * jumlah

        cursor.execute(
            "UPDATE produk SET stok_barang = stok_barang - ? WHERE id = ? AND user_id = ?",
            (jumlah, id_produk, user_id)
        )

        cursor.execute(
            """INSERT INTO penjualan (user_id, id_produk, nama_barang, harga, jumlah, total, tanggal) 
            VALUES (?,?,?,?,?,?,?)""",
            (user_id, id_produk, nama_barang, harga, jumlah, total, tanggal)
        )
        db.commit()
        return 'penjualan telah tercatat'
    
    except:
        db.rollback() # angkah 1 dan 2 diperlakukan sebagai satu paket
        # Kalau salah satu gagal, batalkan semuanya. Itulah rollback.
        raise
        
    finally:
        db.close()

def lihat_daftar_penjualan(user_id, tanggal = None):
    db = koneksi()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    try:
        if tanggal is None:
            cursor.execute("SELECT * FROM penjualan WHERE user_id = ? ORDER BY tanggal DESC",
            (user_id,))

        else:
            cursor.execute("SELECT * FROM penjualan WHERE user_id = ? AND tanggal = ? ORDER BY tanggal DESC",
            (user_id, tanggal))

        data = cursor.fetchall()

        return[
            dict(penjualan)
            for penjualan in data
        ]

    finally:
        db.close()

def laporan_penjualan(user_id, tanggal):
    db = koneksi()
    cursor = db.cursor()

    try:
        cursor.execute(
            """SELECT COALESCE(SUM(total),0) FROM penjualan WHERE user_id = ? AND tanggal = ? """,
            (user_id, tanggal) # coalesce berfungsi untuk memberikan nila 0 jika sum tidak mendapatkan nilai untuk di hitung
            # sehingga bukan nilai null yang di kembalikan 
        )
        hasil_penjualan = cursor.fetchone()[0]

        return {'tanggal': tanggal, 'total_penjualan': hasil_penjualan}

    finally:
        db.close()
