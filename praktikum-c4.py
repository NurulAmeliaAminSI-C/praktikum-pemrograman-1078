import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','7','8']
nim_sambung =''.join(nim)
print(nim)
print()
print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])
print()
print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua)   {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[-len(nim)]}')
print()
data = ['amel',2023,'Aktif']
nilai= [90,89,93,97]
print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])
print()
# >> amel status Kuliah: Aktif
print(f'{data[0]} status Kuliah: {data[2]}')
# >> Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')
# >> Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')
# >> Rata-rata nilai adalah: 92.25
rataan = sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah: {rataan}')
# >> Jumlah nilai mahasiswa adalah: 4
print(f'Jumlah nilai {data[0]} adalah: {len(nilai)}')
print()
print()
#tugas
data   =[['Nurul Amelia Amin',2023,'Aktif'],
         [90,89,93,97,79],
         [20,22],
         ['S1-Reguler', 'sistem informasi B','Ganjil']]
print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print()
matkul = ['Agama islam',
          'pancasila',
          'wawasan cinta iptek dan imtaq',
          'pengantar teknologi informasi',
          'pengantar pemrograman']

matkul.append ('bahasa indonesia') 
matkul.append ('sains terpadu')
matkul.append ('kalkulus dasar')

sks = [2,2,2,3,3]
sks.append ('2')
sks.append ('3')
sks.append ('3')
print(matkul,sks)


print()
print()
#Daftar mata kuliah
print (f'mata kuliah 1: {matkul[0]} dengan jumlah {sks[0]} sks')
print (f'mata kuliah 2: {matkul[1]} dengan jumlah {sks[1]}sks')
print (f'mata kuliah 3: {matkul[2]} dengan jumlah {sks[2]} sks')
print (f'mata kuliah 4: {matkul[3]} dengan jumlah {sks[3]} sks')
print (f'mata kuliah 5: {matkul[4]} dengan jumlah {sks[4]} sks')
print (f'mata kuliah 6: {matkul[5]} dengan jumlah {sks[5]} sks')
print (f'mata kuliah 7: {matkul[6]} dengan jumlah {sks[6]} sks')
print (f'mata kuliah 8: {matkul[7]} dengan jumlah {sks[7]} sks')
print()
print()

print (f'Nama mahasiswa: {data[0][0]}')
print (f'Inisial Nurul Amelia Amin: {data[0][0][0]} {data[0][0][6]} {data[0][0][13]}')
print (f'Nim NUrul Amelia Amin : {nim_sambung}')
print (f'program Nurul Amelia Amin : {data[3][0]}-{data[3][1]}')
print (f'total sks Nurul Amelia Amin adalah: {len(sks)}')
print (f'Jumlah Nilai adalah : {len(data[1])}')
print (f'nilai tertinggi Nurul Amelia Amin :{max(data[1])}')
print (f'nilai terendah Nurul Amelia Amin : {min(data[1])}')
rataan = sum(data[1])/len(data[1])
print (f'rata rata nilai adalah {rataan}')


