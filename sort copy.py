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
    for i in range(n - 1):
        min_id = i
        for j in range(i + 1, n):
            if N[j] < N[min_id]:
                min_id = j
        if min_id != i:
            N[i], N[min_id] = N[min_id], N[i]
        print(f'List setelah putaran i = {i}: {N}')
    return N
if __name__ == '__main__':
    #kumpulan = [10,2,8,7,9]
    #bubble_sort(kumpulan)
    #print(kumpulan)
    kumpulan = [10,2,8,7,9]
    selection_sort(kumpulan)
    print(f'\n{kumpulan}') 

