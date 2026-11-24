#Studi kasus 3
#f. Buat program Python untuk menghasilkan tabel kebenaran.

from itertools import product
import os 
os.system('cls')
def bs(nilai):
    return "B" if nilai else "S"

def tabel_kebenaran():
    print("  p |  q |  r | p∨q |(p∨q)→r")
    hasil = []
    for p, q, r in product([True, False], repeat=3):
        p_atau_q = p or q
        nilai = (not p_atau_q) or r
        hasil.append(nilai)
        print(f'{bs(p), bs(q), bs(r), bs(p_atau_q), bs(nilai)}')
    if all(hasil):
        print("Ekspresi adalah TAUTOLOGI")
    elif not any(hasil):
        print("Ekspresi adalah KONTRADIKSI")
    else:
        print("Ekspresi adalah KONTINGENSI")

tabel_kebenaran()
print('Output sama dengan tabel kebenaran pada bagian a, dan baris terakhir menyatakan bahwa ekspresi adalah kontingensi.')