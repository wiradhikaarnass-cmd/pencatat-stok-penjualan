# Pencatat Stok dan Penjualan (Backend)

API untuk mengelola produk dan mencatat penjualan toko kecil.
Dibuat dengan FastAPI dan SQLite.

## Fitur

- Registrasi dan login (password di-hash dengan bcrypt, autentikasi JWT)
- CRUD produk
- Pencatatan penjualan: stok berkurang otomatis, nama dan harga disalin saat transaksi
- Daftar penjualan dan laporan harian
- Data tiap pengguna terpisah (semua query memakai `user_id` dari token)

## Cara menjalankan

1. Buat dan aktifkan virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
2. Pasang paket:
   ```
   pip install -r requirements.txt
   ```
3. Salin `.env.example` menjadi `.env`, lalu isi `JWT_SECRET` dengan teks acak yang panjang.
4. Jalankan server:
   ```
   uvicorn main:app --reload
   ```
5. Buka dokumentasi interaktif di `http://localhost:8000/docs`.

## Endpoint

Semua endpoint selain registrasi dan login memerlukan header
`Authorization: Bearer <token>`.

| Method | Alamat | Fungsi |
|---|---|---|
| POST | `/registrasi` | Buat akun |
| POST | `/login` | Login, mengembalikan token |
| GET | `/me` | Cek user yang sedang login |
| POST | `/produk` | Tambah produk |
| GET | `/produk` | Daftar produk milik sendiri |
| PUT | `/produk/{id_produk}` | Ubah produk |
| DELETE | `/produk/{id_produk}` | Hapus produk |
| POST | `/penjualan` | Catat penjualan (stok berkurang) |
| GET | `/penjualan?tanggal=YYYY-MM-DD` | Daftar penjualan, tanggal opsional |
| GET | `/penjualan/laporan?tanggal=YYYY-MM-DD` | Total penjualan harian, tanggal wajib |

## Keputusan rancangan

- Nama dan harga produk disalin ke baris penjualan, sehingga riwayat dan
  laporan lama tidak berubah walau harga diubah atau produk dihapus.
- Menghapus produk tidak menghapus riwayat penjualan.
- Pengurangan stok dan penyimpanan penjualan dilakukan dalam satu transaksi
  database (`commit` sekali, `rollback` jika gagal).

## Rencana pengembangan

- Soft delete produk
- Laporan per rentang tanggal
- Pindah ke PostgreSQL dan deploy