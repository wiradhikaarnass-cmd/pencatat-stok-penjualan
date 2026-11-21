import sqlite3
from fastapi import HTTPException
from database.connect import koneksi

def tambah_produk(user_id, nama_barang, harga, stok_barang):
    db = koneksi()
    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO produk (user_id, nama_barang, harga, stok_barang) VALUES(?,?,?,?)",
            (user_id, nama_barang, harga, stok_barang))

        db.commit()
        return 'produk berhasil ditambahkan'

    finally:
        db.close()

def baca_produk(user_id):
    db = koneksi()
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM produk WHERE user_id = ? ORDER BY stok_barang ASC", # order by untuk mengurutkan daftar
        (user_id,))
        data = cursor.fetchall()

        return [
            dict(produk)
            for produk in data
        ]

    finally:
        db.close()

def ubah_data_produk(user_id, id_produk, nama_barang, harga, stok_barang):
    db = koneksi()
    cursor = db.cursor()

    try:
        cursor.execute(
            "UPDATE produk SET nama_barang = ?, harga = ?, stok_barang = ? WHERE id = ? AND user_id = ?",
        (nama_barang, harga, stok_barang, id_produk, user_id))
        db.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code= 404, detail='produk tidak ditemukan')
        
        return 'data produk berhasil diubah'

    finally:
        db.close()

def hapus_produk(user_id, id_produk):
    db = koneksi()
    cursor = db.cursor()

    try:
        cursor.execute("DELETE FROM produk WHERE id = ? AND user_id = ?",
        (id_produk, user_id))       
        db.commit()

        data = cursor.rowcount

        if data == 0:
            raise HTTPException(status_code=404, detail='produk tidak ditemukan')

        return {'id_produk': id_produk, 'pesan':'data produk berhasil dihapus'}

    finally:
        db.close()