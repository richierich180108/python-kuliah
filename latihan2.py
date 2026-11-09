import os 
os.system('cls')
print('=='*3, 'PEMBERIAN BEASISWA', '=='*3)


while True:
    tingkat_pendidikan = str(input('apa pendidikan terakhir kamu(sma/s1/s2): '))

    if tingkat_pendidikan == 'sma':
        nilai = float(input('masukkan nilai: '))
        if nilai >= 90:
            print('Beasiswa 100%')
        elif nilai >= 80 and nilai <=89:
            print('Beasiswa 50%')
        else:
            print('Tidak mendapatkan beasiswa')
    elif tingkat_pendidikan == 's1':
        ipk = float(input('masukkan ipk: '))
        if ipk >= 3.75:
            print('Beasiswa 100%')
        elif ipk >= 3.25 and ipk <=3.74:
            print('Beasiswa 75%')
        else:
            print('Beasiswa 30%')
    elif tingkat_pendidikan == 's2':
        ipk = float(input('masukkan ipk: '))
        if ipk >= 3.8:
            print('Beasiswa 100%')
        elif ipk >= 3.5 and ipk <=3.79:
            print('Beasiswa 50%')
        else:
            print('Beasiswa 30%')
    else: 
        print('salah input coba lagi')
        continue
    break





