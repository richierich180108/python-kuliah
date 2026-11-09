import os
os.system('cls')
import test


age = int(input('masukan umur : '))
bmi = float(input('masukan BMI : '))

if age < 45 and bmi < 22:
    print('low')
elif age <45 and bmi >= 22 or age >= 45 and bmi <22:
    print('medium')
else:
    print('high')
