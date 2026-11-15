# BAB 14: POLYMORPHISM

# 1. Polymorphism pada Method
class Kucing:
    def suara(self):
        return "Meow"


class Anjing:
    def suara(self):
        return "Guk guk"


hewan = [Kucing(), Anjing()]

for h in hewan:
    print(h.suara())


# 2. Polymorphism dengan Inheritance
class Hewan:
    def suara(self):
        return "Hewan bersuara"


class Burung(Hewan):
    def suara(self):
        return "Cuit cuit"


daftar_hewan = [Kucing(), Anjing(), Hewan(), Burung()]

for h in daftar_hewan:
    print(h.suara())


# 3. Polymorphism dengan Fungsi
def cetak_suara(hewan):
    print(hewan.suara())


cetak_suara(Kucing())
cetak_suara(Anjing())


# 4. Polymorphism dengan Built-in Function
print(len("Python"))
print(len([1, 2, 3]))
print(len({"nama": "Aris", "kelas": "XI"}))
