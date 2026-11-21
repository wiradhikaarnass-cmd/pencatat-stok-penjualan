import bcrypt

# ini adalah fungsi yang digunakan ketika membuat akun
def buat_hash(password):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt)

    return password_hash

# fungsi yang digunakan untuk mengecek akun saat ingin login (kita perlu mengecek hash password)
def cek_hash(password, password_hash):
    return bcrypt.checkpw(password.encode(), password_hash.encode())