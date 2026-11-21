from pydantic import BaseModel, field_validator

# ini adalah fungsi yang digunakan ketika membuat akun
class UserInput(BaseModel):
    username : str
    password : str

    @field_validator('password')
    @classmethod
    def cek_panjang_password(cls, nilai):
        if len(nilai.encode()) > 72:
            raise ValueError ('password terlalu panjang (max 72 bytes)')
        return nilai