import os
import random
os.system('cls')


print('='*6,'classy animal','='*6)
print('pilih menu: \n1. Insert Animal\n2. exit')

while True :
    pilihan = input('pilih (1/2): ')
    match pilihan:
        case '1':
            name = input('masukkan nama: ')
            if name.isalpha():
                age = input('masukkan umur: ')
                habitat = input('air, darat, udara, amphibi: ')
                weight = float(input('masukkan berat badan: '))
                height = float(input('masukkan tinggi: '))
                BMI = weight/(height**2)
                animal = [f'\nname: {name}\n age: {age}\n habiat: {habitat}\n weight: {weight}\n height: {height}\n BMI: {BMI}']
                for i in animal:
                    print(f'{i}\n')
            else:
                print('masukkan lagi tanpa angka')
                continue
        case _:
            break


