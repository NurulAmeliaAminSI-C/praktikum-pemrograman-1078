nama= 'nurul amelia amin'
nim = '231031078'
meet= 'praktikum 3 (string)'
prodi='Sistem Informasi C'
email='amelianurul632@gmail.com'
ttl= 'parepare,30-agustus-2005'
alamat='jalan bau massepe'
asal= 'parepare'
hobi='membaca'
tinggi='153'
print ('-'*110)
strl= 'nurul amelia amin'


sp=40
print ('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print (meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-'*sp)

print (f"""\thalo nama saya {nama} dengan nim {231031078} dari prodi {prodi}, ini adalah file {meet}.string.terimakasih.\n""")
print (f"""biodata saya,
Nama\t: (Nama)
nim\t: (Nim)
prodi\t:(prodi)
TTL\t: (Asal)
Asal\t:(kota)
hobi\t:(hobi)
Tinggi\t:(tinggi cm
""")

stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir
a = stat1.split()
stat1 = ' '.join([a[-1], a[0], a[1], a[2]])
print(stat1)
print()

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac
a = stat2.split()
stat2 = ' '.join(['duFort'[0], 'Frankel'[0], 'Sir'[0], 'Issac'])
print(stat2)
print()

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I
stat3 = ' '.join(['duFort', 'Frankel'[0], 'Sir'[0], 'Issac'[0]])
print(stat3)
print()

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir
a = stat4.split()
stat4 = ' '.join([a[-1][0], a[0], a[1], a[2]])
print(stat4)
print()

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S
a = stat5.split()
stat5 = ' '.join([a[-1], a[0][0], a[1][0], a[2][0]])
print(stat5)
print()

stat6 = ['duFort Frankel Sir Issac']
# ISSAC D F S
stat6 = ' '.join([a[-1], a[0][0], a[1][0], a[2][0]]).upper()
print(stat6)
print()

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac
a =stat7.strip ('#,$')
print(a)
print()

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac
b = a.strip ('#,$')
print(b)
print()

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac
b = a.strip ('#,@,$')
print(b)
print()
