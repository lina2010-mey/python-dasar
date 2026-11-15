# BAB 6: OPERATOR PYTHON

# 1. Operator Aritmatika
a = 10
b = 3

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Modulus:", a % b)
print("Pangkat:", a ** b)

# 2. Operator Perbandingan
x = 5
y = 10

print("\nSama dengan:", x == y)
print("Tidak sama dengan:", x != y)
print("Lebih besar:", x > y)
print("Lebih kecil:", x < y)
print("Lebih besar sama dengan:", x >= y)
print("Lebih kecil sama dengan:", x <= y)

# 3. Operator Logika
a = True
b = False

print("\nAND:", a and b)
print("OR:", a or b)
print("NOT:", not a)

# 4. Operator Penugasan
x = 10
x += 5
print("\nTambah:", x)
x -= 3
print("Kurang:", x)
x *= 2
print("Kali:", x)
x /= 4
print("Bagi:", x)

# 5. Operator Keanggotaan
buah = ["apel", "jeruk", "mangga"]

print("\nApel tersedia:", "apel" in buah)
print("Pisang tidak tersedia:", "pisang" not in buah)

# 6. Operator Identitas
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\nA dan B objek sama:", a is b)
print("A dan C objek sama:", a is c)
print("A dan C nilainya sama:", a == c)
