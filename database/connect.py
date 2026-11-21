import sqlite3

def koneksi():
    db = sqlite3.connect('penjualan.db')
    return db

# ini adalah fungsi yang digunakan ketika membuat akun
def buat_tabel():
    db = koneksi()
    db.execute(
        """CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL)"""
    )

    db.execute(
        """CREATE TABLE IF NOT EXISTS produk(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        nama_barang TEXT NOT NULL,
        harga INTEGER NOT NULL,
        stok_barang INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id))"""
    )

    db.execute(
        """CREATE TABLE IF NOT EXISTS penjualan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        id_produk INTEGER NOT NULL,
        nama_barang TEXT NOT NULL,
        harga INTEGER NOT NULL,
        jumlah INTEGER NOT NULL,
        total INTEGER NOT NULL,
        tanggal TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (id_produk) REFERENCES produk(id))"""
    )

    db.commit()
    db.close()