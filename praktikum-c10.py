import os
 
def judul():
    os.system('cls')
    print('program menghitung volume dan luas permukaan')
    print('bangun ruang kubus')
    print()

def inputan():
   p = float(input('masukkan panjang: '))
   l = float(input('masukkan lebar: '))
   t = float(input('masukkan tinggi: '))
   return p,l,t

def tampilkan(jenis,nilai):
    print(f'nilai dari {jenis} adalah : {nilai}')
   
def perhitungan(p,l,t):
    vol = p * l * t
    luas = 2 * (p*l + p*t + l*t)
    luas_non_tutup = luas - p*l
    return vol,luas,luas_non_tutup


def pilihan():
    pilih = input('apakah lanjutkan? [y/n]')
    if pilih == 'y':
        a  = True
    else:
        a = False
        print('sampai jumpa lagi')
    return a



def main():
    judul()                                       #judul
    p,l,t = inputan()                             #inputan
    vol,luas,luas_non_tutup = perhitungan(p,l,t)  #perhitungan
    #tampilkan
    tampilkan('volume',vol)
    tampilkan('luas permukaan', luas)
    tampilkan('luas permukaan tanpa tutup',luas_non_tutup)
    
    a = pilihan()    # pilihan

a = True
while a:
    main()
