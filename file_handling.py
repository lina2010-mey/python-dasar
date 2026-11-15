# BAB 17: FILE HANDLING

# 1. Menulis file
with open("data.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")
    file.write("Saya sedang belajar File Handling.\n")


# 2. Menambahkan data
with open("data.txt", "a") as file:
    file.write("Ini adalah baris tambahan.\n")


# 3. Membaca seluruh isi file
print("Isi file:")
with open("data.txt", "r") as file:
    print(file.read())


# 4. Membaca file baris per baris
print("Membaca per baris:")
with open("data.txt", "r") as file:
    for baris in file:
        print(baris.strip())
