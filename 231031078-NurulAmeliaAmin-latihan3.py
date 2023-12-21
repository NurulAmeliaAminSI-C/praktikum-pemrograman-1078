nama = input("Masukkan nama karyawan: ")
pendapatan = int(input("Masukkan pendapatan karyawan: "))

print("Nama karyawan:", nama)
print("Pendapatan karyawan:", pendapatan)

if pendapatan > 7000:
    print("Status: Berhak")
else:
    print("Status: Tidak Berhak")