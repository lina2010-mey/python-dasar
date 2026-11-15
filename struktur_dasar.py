# BAB 2: STRUKTUR DASAR PROGRAM PYTHON

# 1. Komentar satu baris
# Ini adalah komentar

# 2. Komentar multi-baris
"""
Ini komentar multi-baris.
Biasa dipakai untuk dokumentasi.
"""

# 3. Indentasi
if True:
    print("Kode ini berada di dalam blok if")
    print("Masih di dalam blok if")

print("Kode ini sudah di luar blok if")

# 4. Input dan Output
nama = input("Masukkan nama Anda: ")
print("Halo,", nama)

# 5. Fungsi main
def main():
    print("Hello dari fungsi main!")

if __name__ == "__main__":
    main()
