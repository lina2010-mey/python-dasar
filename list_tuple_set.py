# BAB 9: LIST, TUPLE, DAN SET

# 1. List
buah = ["apel", "jeruk", "mangga"]

print("List awal:", buah)
print("Buah pertama:", buah[0])

buah.append("pisang")
buah[1] = "anggur"
buah.remove("mangga")

print("List setelah diubah:", buah)

# 2. Tuple
warna = ("merah", "hijau", "biru")

print("\nWarna kedua:", warna[1])

for w in warna:
    print(w)

# 3. Set
angka = {1, 2, 3, 3, 4, 5}

print("\nSet awal:", angka)

angka.add(6)
angka.remove(2)

print("Set setelah diubah:", angka)

# 4. Operasi himpunan
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}

print("Union:", ganjil | genap)
print("Intersection:", ganjil & genap)
print("Difference:", ganjil - genap)
