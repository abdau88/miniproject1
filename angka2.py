# Fungsi untuk input data
def input_angka():
    angka = int(input("Masukkan sebuah angka: "))
    return angka

# Fungsi untuk memproses data (menentukan ganjil atau genap)
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print("Angka genap")
    else:
        print("Angka ganjil")

# Program utama
bilangan = input_angka()       # memanggil fungsi input
cek_ganjil_genap(bilangan)     # memanggil fungsi proses
