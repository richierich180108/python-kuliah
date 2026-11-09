import os
os.system('cls')


def bubble_sort(kumpulan:list):
    n = len(kumpulan)
    count = 0 
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            count = count+1
            if kumpulan[j] > kumpulan[j+1]:
                kumpulan[j],kumpulan[j+1] = kumpulan[j+1],kumpulan[j]
                swapped = True
        if not swapped:
            print('looping stop when i = ',i,'j = ', j)
            break
    print('jumlah langkah = ', count)
    return kumpulan

def selection_sort(N: list):
    n = len(N)
    print(f'List awal: {N}')
    print(f'Jumlah elemen (n) = {n}')
 
    for i in range(n - 1):
        min_id = i
        print(f'\n=== Putaran i = {i} ===')
        print(f'Anggap N[{i}] = {N[i]} paling kecil, jadi min_id = {min_id}')
 
        for j in range(i + 1, n):
            print(f'  j = {j}: bandingkan N[{j}] = {N[j]} dengan N[min_id] = N[{min_id}] = {N[min_id]}')
            if N[j] < N[min_id]:
                min_id = j
                print(f'    -> lebih kecil, min_id berubah menjadi {min_id}')
            else:
                print(f'    -> tidak lebih kecil, min_id tetap {min_id}')
 
        if min_id != i:
            print(f'Tukar N[{i}] = {N[i]} dengan N[{min_id}] = {N[min_id]}')
            N[i], N[min_id] = N[min_id], N[i]
        else:
            print(f'min_id sama dengan i, N[{i}] = {N[i]} sudah di posisi benar, tidak ditukar')
 
        print(f'List setelah putaran i = {i}: {N}')
 
    return N
if __name__ == '__main__':
    #kumpulan = [10,2,8,7,9]
    #bubble_sort(kumpulan)
    #print(kumpulan)
    kumpulan = [10,2,8,7,9]
    selection_sort(kumpulan)
    print(f'\n{kumpulan}') 

