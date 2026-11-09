import os 
os.system('cls')

#recursion
def faktorial_r(n):
    if n < 0:
        raise ValueError('faktorial is not defined')
    if n == 0 or n ==1:
        return 1
    else:
        return n * faktorial_r(n-1)

def factorial_i(n):
    if n < 0:
        raise ValueError('factorial is not defined')
    result = 1
    while n >= 1:
        result = result * n 
        n = n - 1
    return result

if __name__ == '__main__':
    hasil = faktorial_r(int(input('masukkan angka: ')))
    print(hasil)
    hasil1 = factorial_i(int(input('masukkan angka: ')))
    print(hasil1)
    