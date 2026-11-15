# BAB 18: MODULE

# 1. Menggunakan import
import matematika

print("Penjumlahan:", matematika.tambah(2, 3))
print("Perkalian:", matematika.kali(4, 5))


# 2. Menggunakan alias
import matematika as m

print("Dengan alias:", m.tambah(10, 5))


# 3. Import fungsi tertentu
from matematika import tambah

print("From import:", tambah(7, 3))


# 4. Built-in module
import math

print("Akar kuadrat:", math.sqrt(16))
print("Nilai PI:", math.pi)
