#lanjut bahas tuple, set, dictionary
import hashlib 
vowel = {1,2,4,7,3,3,5,8,4,5,6,7,3,4}
print(vowel)
vowel.add('ys')
print(vowel)

base = ('a','c','b','d')
print(base)


#dasar dari programming sebenrnya adalah tipe data, variabel, koleksi data(dalam bahasa lain array),perkondisian, dan perlogikaan
#lanjut ke function 


def get_weekday(current_day, days_ahead):
    return(current_day+days_ahead) %7 

print(get_weekday(6,3))
tanggal_hari_ini = int(input('masukkan angka: '))
def berapa_hari_lagi_tahun_baru(tanggal_hari_ini):
    return (365%tanggal_hari_ini)

print(berapa_hari_lagi_tahun_baru(tanggal_hari_ini))
