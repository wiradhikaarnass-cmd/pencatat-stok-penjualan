pertama = kita membuat fitur registrasi/membuat akun
- disini kita menggunakan query sql INSERT
- dani kita membutuhkan fungsi untuk membuat hash pada password (sevices.security_hash)
- juga membutuhkan basemodel sebagai pembuatan objek/karakteristik yang dimiliki oleh (username, password)(models.user)

kedua = kita membuat fitur login/masuk ke akun kita
- disini kita menggunakan query sql SELECT 
- dan kita membutuhkan pengecekan hash pada password yang kita buat sebelumnya(services.security_hash)

ketiga = kita membuat fitur pembuatan token
didalam penggunaan nya secara nyata, kita mengibaratkan fungsi token ini untuk menentukan berapa lama kita bisa berada
didalam sebuah aplikasi, yang dimana jika tokennya sudah habis, maka kita akan keluar dengan sendirinya

** Alur Program **
<ALUR REGISTRASI DAN LOGIN AKUN>
1. kita membuat akun di <folder services>, memasukan username dan password ke dalam sql, tapi sebelum ia masuk ke sql, kita menvalidasinya dulu menggunakan <pydantic di folder models>, jika sesuai dengan objek yang kita tetapkan, maka alurnya akan lanjut ke pembuatan hash untuk password di <folder services.security_hash>, lalu hash nya di simpan di tabel users
2. kemudian kita login, saat memasukan akun kita melakukan pengecekan hash di <foder services.security_hash>, saat hash nya sesuai dengan yang ada ditabel, maka kita melakukan pembuatan token di <folder services.token>
3. Sebelum program dijalankan, kita membuat secret_key sekali saja dan menyimpannya di .env. Saat login berhasil, program membaca secret itu untuk menandatangani token baru.
4. oke setelah pembuatan tokennya selesai, dia akan mengembalikan token tersebut ke client yang akan di salin untuk digunakan
5. saat kita ingin masuk ke endpoint berikutnya kita memasukan token yang sudah kita salin ini, lalu token tersebut dijadikan sebagai header authorization, karna Token yang kita salin ditaruh di header Authorization: Bearer <token>. Saat request masuk, HTTPBearer mengambil token dari header itu, lalu cek_token menghitung ulang signature dengan secret_key dan mengecek masa berlaku. Kalau lolos, sub diambil dan dikembalikan sebagai int, lalu masuk ke parameter user_id di router.

