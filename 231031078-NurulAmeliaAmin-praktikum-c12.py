import os
os.system('cls')

#Fungsi Rekursif factorial dengan perulangan 
def faktorial(nilai): 
   if nilai<=1:
      return 1
   else:
      return nilai*faktorial(nilai-1) 
#Program Utama 
for i in range(11): 
   print('%2d ! = %d' % (i,faktorial(i))) 



# PROGRAM BAGIAN KEDUA
# Fungsi Rekursif factorial 
def faktorial(nilai):
    if nilai <= 1: 
        return 1
    else:
        return nilai * faktorial(nilai-1)

# Input bilangan dari user   
bil = int(input("Masukkan bilangan: "))

# Tampilkan hasil faktorial
print(f"{bil}! = {faktorial(bil)}")