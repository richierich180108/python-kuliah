import os
from typing import List, Tuple
import time
import pert_8

os.system('cls')

def findv1(L: list[float])->Tuple[int,int]:
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    if min1 <= min2:
        min2+=1
    return (min1,min2)

def findv2(L: list[float])->Tuple[int,int]:
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)
    return (min1,min2)

def findv3(L: list[float])->Tuple[int,int]:
    if L[0] < L[1]:
        min1, min2 = 0,1
    else:
        min1,min2 = 1,0
    for i in range(2,len(L)):
        if L[i]<L[min1]:
            min2=min1
            min1=i
        elif L[i]<L[min2]:
            min2 = i
    return (min1,min2)

if __name__ == '__main__':
    dataset1 = []
    dataset2 =[]
    dataset3 = []
    
    dataset_file = open('data.txt','r')
    for line in dataset_file:
        dataset1.append(float(line))
        dataset2.append(float(line))
        dataset3.append(float(line))
    dataset_file.close()

    t1 = time.perf_counter()
    minv11, minv12 = findv1(dataset1)
    t2 = time.perf_counter()
    total_timev1 = (t2-t1) * 1000

    t1 = time.perf_counter()
    minv21, minv22 = findv2(dataset2)
    t2 = time.perf_counter()
    total_timev2 = (t2-t1) * 1000

    t1 = time.perf_counter()
    minv31, minv32 = findv3(dataset3)
    t2 = time.perf_counter()
    total_timev3 = (t2-t1) * 1000


    print("Cara 1: {0:.2f}ms, hasilnya = {1}, {2}".format(total_timev1,minv11,minv12)) 
    print("Cara 2: {0:.2f}ms, hasilnya = {1}, {2}".format(total_timev2,minv21,minv22)) 
    print("Cara 3: {0:.2f}ms, hasilnya = {1}, {2}".format(total_timev3,minv31,minv32)) 


