#studi kasus 4
#f. Buat program Python untuk menghasilkan tabel kebenaran.
from itertools import product
import os
os.system('cls')
def bs(nilai):
    return "B" if nilai else "S"

def tabel_kebenaran():
    print(" p  |  q  | r | p∧q |(p∧q)→r")
    hasil = []
    for p, q, r in product([True, False], repeat=3):
        p_dan_q = p and q
        nilai = (not p_dan_q) or r
        hasil.append(nilai)
        print(f'{bs(p), bs(q), bs(r), bs(p_dan_q), bs(nilai)}')
    if all(hasil):
        print("Ekspresi adalah TAUTOLOGI")
    elif not any(hasil):
        print("Ekspresi adalah KONTRADIKSI")
    else:
        print("Ekspresi adalah KONTINGENSI")

tabel_kebenaran()
print('Output sama dengan tabel kebenaran pada bagian a. \nHanya baris 2 yang bernilai S, dan program menyimpulkan bahwa ekspresi adalah kontingensi.')