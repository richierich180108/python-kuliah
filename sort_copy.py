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
    print(f'isi list awal {N}')
    for i in range(n - 1):
        min_id = i
        for j in range(i + 1, n):
            if N[j] < N[min_id]:
                min_id = j
        if min_id != i:
            N[i], N[min_id] = N[min_id], N[i]
        print(f'isi list sekarang {N}')
    return N

def quick_sort_simple(arr:list):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_simple(left) + middle + quick_sort_simple(right)

def copy_quick_sort(L:list,):
    workspace = quick_sort_simple(L)
    if len(workspace) != 0:
        L[:] = workspace


def partition(collection:list, low:int, high:int):
    pivot = collection[high]
    i = low - 1
    for j in range(low,high):
        if collection[j] <= collection[pivot]:
            i += 1 
            collection[i],collection[j] = collection[j],collection[i]
    collection[i+1],collection[high] = collection[high],collection[i+1]
    return i + 1

def quick_sort_r(basket: list, low, high):
    if low<high:
        p = partition(basket,low,high)
        quick_sort_r(basket,low,p-1)
        quick_sort_r(basket,p+1,high)

def merge(left:list, right:list)->list:
    Lbar = []
    i1 = 0
    i2 = 0
    while i1 != len(left) and i2 != len(right):
        if left[i1] <= right[i2]:
            Lbar.append(left[i1])
            i1 +=1
        else:
            Lbar.append(right[i2])
            i2 +=1
    Lbar.extend(left[i1:])
    Lbar.extend(right[i2:])
    return Lbar

def merge_sort(golongan:list):
    ws = []
    for i in range(len(golongan)):
        ws.append([golongan[i]])
    i = 0
    while i < len(ws) -1:
        left = ws[i]
        right = ws[i+1]
        lbar = merge(left,right)
        ws.append(lbar)
        i += 2
    if len(ws)!= 0:
        golongan[:] = ws[-1][:]

if __name__ == '__main__':
    #kumpulan = [10,2,8,7,9]
    #bubble_sort(kumpulan)
    #print(kumpulan)
    kumpulan = [10,2,8,7,9]
    #quick_sort_r(kumpulan)
    #copy_quick_sort(kumpulan)
    merge_sort(kumpulan)
    print(kumpulan)
