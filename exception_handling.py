# BAB 16: EXCEPTION HANDLING

# 1. Try dan Except
try:
    angka = 10
    hasil = angka / 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")


# 2. Menangani ValueError
try:
    data = int("abc")
except ValueError:
    print("Error: Data tidak valid!")


# 3. Else dan Finally
try:
    angka = 10 / 2
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")
else:
    print("Perhitungan berhasil, hasil:", angka)
finally:
    print("Selesai memproses.")


# 4. Membuat Exception Sendiri
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    else:
        print("Umur valid:", umur)


try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)
