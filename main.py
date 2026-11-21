from fastapi import FastAPI 
from routers.auth import router
from routers.produk import router as router_produk
from routers.penjualan import router as router_penjualan

from database.connect import buat_tabel

app = FastAPI()

buat_tabel()

app.include_router(router)
app.include_router(router_produk)
app.include_router(router_penjualan)