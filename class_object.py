# BAB 11: CLASS & OBJECT

# 1. Membuat Class dan Object
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")


mhs1 = Mahasiswa("Budi", "Informatika")
mhs2 = Mahasiswa("Siti", "Sistem Informasi")

mhs1.sapa()
mhs2.sapa()


# 2. Atribut dan Method
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


pp = PersegiPanjang(5, 3)

print("Luas:", pp.luas())
print("Keliling:", pp.keliling())
