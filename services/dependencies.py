from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.token_services import cek_token

skema = HTTPBearer() # library ini digunakan untuk membaca, dan membagi header authorization menjadi bearer dengan token

def user_saat_ini(kredensial: HTTPAuthorizationCredentials = Depends(skema)): # skema dijalankan duluan di function ini karna
# ada kode Depends yang merupakan kode bawaan fastapi untuk menjalankan kode lebih dulu dibanding yang lainnya
# setelah kode tersebut dijalankan sesuai fungsinya, kita memasukannya ke dua wadah yang telah disiapkan yaitu
# HTTPAuthorizationCredentials, lalu kita masukan lagi ke parameter fungsi ini
# adapun wadahnya ini credensials sebagai wadah dari token, olehnya saat ingin di cek wadah ini di panggil

    data = cek_token(kredensial.credentials)

    if data is None:
        raise HTTPException (status_code=401, detail='token tidak valid atau sudah kadaluarsa')

    return int(data['sub'])