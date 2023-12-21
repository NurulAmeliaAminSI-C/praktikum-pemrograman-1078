import os
os.system('cls')

# program bagian pertama
# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print("Tidak ada bilangan yang bernilai negatif") 
    elif n == 0 or n == 1:
        return n  
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Program Utama
nilai = 20
hasil = fibonacci(nilai)
print('Fibonacci(%d)=%d' % (nilai, hasil))


# program bagian kedua
# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print("Bilangan fibonacci tidak defined untuk bilangan negatif")
    elif n == 0 or n == 1:
        return n  
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Input nilai n 
n = int(input("Masukkan nilai n: "))  

# Hitung Fibonacci ke-n
hasil = fibonacci(n)

# Tampilkan hasil
print("Fibonacci ke-%d adalah %d" % (n, hasil))