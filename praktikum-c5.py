import os
os.system('clear')

a = True
limit = 5 
i = 0              
while a:
    i += 1      
    print (f'menjalankan program {limit + 1 - i}')
    if i == limit:
        a = False
        print ('program berhenti di sini!')
    else:
        a = True