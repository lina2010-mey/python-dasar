# BAB 10: DICTIONARY PYTHON

# 1. Membuat Dictionary
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)

# 2. Mengakses Data
print("\nNama:", mahasiswa["nama"])
print("Umur:", mahasiswa.get("umur"))

# 3. Menambah dan Mengubah Data
mahasiswa["angkatan"] = 2023
mahasiswa["umur"] = 21

print("\nData setelah diubah:", mahasiswa)

# 4. Menghapus Data
mahasiswa.pop("jurusan")
del mahasiswa["nama"]

print("\nData setelah dihapus:", mahasiswa)

# 5. Iterasi Dictionary
for key, value in mahasiswa.items():
    print(key, ":", value)

# 6. Nested Dictionary
kampus = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print("\nNama mahasiswa:", kampus["mahasiswa1"]["nama"])
