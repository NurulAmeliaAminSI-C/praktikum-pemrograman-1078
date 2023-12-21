''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir',
            'S1',
            'Sistem Informasi C',
            'aktif',
            'ganjil',
            '2023-2024',
            'kartu hasil studi mahasiswa']
#(NOTED: sesuaikan dengan data anda)

2. 1. Buat variabel jenis list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi C
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''


# Tulis Kode Jawaban di bawah!
# Definisikan variabel Bio
Bio = ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'Nurul Amelia Amin',
            '231031066',
            '30-08-2005',
            'S1',
            'Sistem Informasi C',
            'aktif',
            'ganjil',
            '2023-2024',
            'kartu hasil studi mahasiswa']

MK = [['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta IPTEK dan IMTAQ','Pengantar Pemograman','Pengantar Teknologi Informasi','Kalkulus Dasar 1','Sains Terpadu'],
        [2,2,2,2,3,3,3,3],
        ['22B0211012','22B0211022','22B0211032','22B0211042','22B0211073','22B0211063','22B0211083','22B0211053'],
        [3.75,3.75,3.50,4.00,3.00,3.00,3.50,3.75]]

print(Bio[0].upper().center(71))
print(Bio[2].upper().center(71))
print(Bio[-1].upper().center(71))
strr = Bio[-3]+' '+Bio[-2].replace('-','/')
print(strr.upper().center(71))

print(f'''
Nama Lengkap    : {Bio[3].upper()}
NIM             : {Bio[4]}
Program/prodi   : {Bio[6]}/{Bio[7]}
Tahun Masuk     : {Bio[-2][:4]} {Bio[-3].title()}
Status          : {Bio[-4]}''')

print('|--|--  12  --|--            31            --|-- 7 --|-- 13 --|')
print('-'*61)
print('No.'+'|'+'KODE'.ljust(10)+'|'+'MATA KULIAH'.center(30)+'|'+'SKS'.center(7)+'|'+'NILAI'.center(8)+'|')
print('-'*61)
print('1. '+'|'+'22B0211012'.ljust(10)+'|'+'Agama Islam'.center(30)+'|'+'2'.center(7)+'|'+'3.75'.center(8)+'|')
print('2. '+'|'+'22B0211022'.ljust(10)+'|'+'Pancasila'.center(30)+'|'+'2'.center(7)+'|'+'3.75'.center(8)+'|')
print('3. '+'|'+'22B0211032'.ljust(10)+'|'+'Bahasa Indonesia'.center(30)+'|'+'2'.center(7)+'|'+'3.50'.center(8)+'|')
print('4. '+'|'+'22B0211042'.ljust(10)+'|'+'Wawasan Cinta IPTEK dan IMTAQ'.center(30)+'|'+'2'.center(7)+'|'+'4.00'.center(8)+'|')
print('5. '+'|'+'22B0211073'.ljust(10)+'|'+'Pengantar Pemograman'.center(30)+'|'+'3'.center(7)+'|'+'3.00'.center(8)+'|')
print('6. '+'|'+'22B0211063'.ljust(10)+'|'+'Pengantar Teknologi Informasi'.center(30)+'|'+'3'.center(7)+'|'+'3.00'.center(8)+'|')
print('7. '+'|'+'22B0211083'.ljust(10)+'|'+'Kalkulus Dasar 1'.center(30)+'|'+'3'.center(7)+'|'+'3.50'.center(8)+'|')
print('8. '+'|'+'22B0211053'.ljust(10)+'|'+'Sains Terpadu'.center(30)+'|'+'3'.center(7)+'|'+'3.75'.center(8)+'|')
print('-'*61)

pt = 61
print(f"\t\t\t\t       TOTAL SKS:   {sum(MK[1])}")
print('-'*pt)
a = "71"
print(f"|{a.center(pt,'-')}|")
print("Summary:")
print(f"Jumlah Mata Kuliah\t: {len(MK[0])} Mata Kuliah")
print(f"Nilai Tertinggi\t\t: {max(MK[-1])}0 ({MK[-2][3]} - {MK[0][3]})")
print(f"Nilai Terendah\t\t: {min(MK[-1])}0 ({MK[-2][-1]} - {MK[0][-1]})")
print("IP Kumulatif\t\t: 3.00")
print(f"{'Parepare, 30 agustus 2005':>70}\n")
print(f"\n{'Nurul Amelia Amin':>70}\n{'-'*70}")