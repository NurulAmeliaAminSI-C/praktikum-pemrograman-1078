import os
os.system('cls')


# Bagian ppertama
nilai = 5

def hitung_faktorial(nilai):
    # Mencari Faktorial dengan input 
    if nilai > 1:
        return nilai * hitung_faktorial(nilai-1)
    return 1

# program utama
faktorial = hitung_faktorial(nilai)
print(f'Nilai Faktorial dari {nilai}! = {faktorial}')

# program kedua
def hitung_faktorial(nilai):
    if nilai > 1:
        return nilai * hitung_faktorial(nilai-1)
    return 1

# Input nilai 
nilai = int(input("Masukkan nilai: "))  

# menghitung faktorial
faktorial = hitung_faktorial(nilai)

# Tampilkan hasil
print(f"Faktorial dari {nilai} adalah {faktorial}")
