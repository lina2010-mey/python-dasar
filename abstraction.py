# BAB 15: ABSTRACTION

from abc import ABC, abstractmethod


# Abstract class
class Hewan(ABC):

    @abstractmethod
    def suara(self):
        pass


# Subclass
class Kucing(Hewan):
    def suara(self):
        return "Meow"


class Anjing(Hewan):
    def suara(self):
        return "Guk guk"


# Membuat object
kucing = Kucing()
anjing = Anjing()

print(kucing.suara())
print(anjing.suara())


# Contoh abstraction pada sistem pembayaran
class Pembayaran(ABC):

    @abstractmethod
    def bayar(self, jumlah):
        pass


class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")


class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")


# Menjalankan pembayaran
def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)


proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Dana(), 75000)
