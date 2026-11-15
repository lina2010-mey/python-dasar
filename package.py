# BAB 19: PACKAGE

# 1. Menggunakan package
from my_package import operasi, geometri

print("Pengurangan:", operasi.kurang(10, 4))
print("Luas persegi:", geometri.luas_persegi(5))


# 2. Import fungsi tertentu
from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print("Import fungsi kurang:", kurang(20, 7))
print("Import fungsi luas:", luas_persegi(8))


# 3. Package bawaan Python
import os
import datetime

print("Folder saat ini:", os.getcwd())
print("Tanggal hari ini:", datetime.date.today())
