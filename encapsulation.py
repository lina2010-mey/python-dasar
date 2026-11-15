# BAB 12: ENCAPSULATION

class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal

    # Getter
    def lihat_saldo(self):
        return self.__saldo

    # Setter melalui method setor
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")


# Membuat object
akun = BankAccount(1000)

print("Saldo awal:", akun.lihat_saldo())

akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())

akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())
