import os 
os.system('cls')

def linear_w(L: list, value: int):
    i = 0
    print(L[i])
    while i != len(L) and L[i] != value:
        i = i+1
    if i == len(L):
        return -1
    else:
        return i


def linear_f(L: list, value: int):
    for i in range(len(L)):
        if L[i] == value:
            return i 
    return -1

def binary(L:list, value: int):
    sort_list = sorted(L)
    i = 0
    j = len(sort_list) - 1
    while i != j+1:
        m = (i+j)//2
        if sort_list[m] < value:
            i = m + 1 
        else:
            j = m-1 
    if 0 <= i < len(sort_list) and sort_list[i] == value:
            return L.index(value)
    else:
        return -1   


print(linear_w([1,4,3,6,8,9,6,35,24],6))
print(linear_f([1,4,3,6,8,9,6,35,24],6))
print(binary([1,4,3,6,8,9,6,35,24],24))
if __name__ == '__main__':
    array =  [4,1,7,3,9]
    print(linear_w(array,7))
    print(linear_f(array,7))
    print(binary(array,7))