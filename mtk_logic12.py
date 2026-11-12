#412026006 - Richie
#tugas Logic mtk 12 
import os
import numpy as np
os.system('cls')

'''Soal 1 - Estimasi Mean
Sebuah aplikasi mobile diuji untuk mengetahui penggunaan memori RAM. Dari 8 kali pengujian diperoleh data (MB):
120, 135, 125, 140, 130, 150, 125, 135
Hitung estimasi titik rata-rata penggunaan RAM aplikasi.'''

#Estimasi mean
Penggunaan_memori_RAM = np.array([120, 135, 125, 140, 130, 150, 125, 135]) 
rata_rata  = np.mean(Penggunaan_memori_RAM)
print(f'Estimasi titik rata-rata penggunaan RAM adalah {rata_rata} MB\n')

'''Soal 2 - Estimasi Proporsi
Dari 300 pengguna aplikasi e-commerce, sebanyak 240 pengguna berhasil menyelesaikan transaksi tanpa error.
Hitung estimasi proporsi pengguna yang berhasil menyelesaikan transaksi.
'''

#Estimasi proporsi
pengguna_aplikasi = 300
pengguna_berhasil_transaksi = 240
proporsi_estimasi = pengguna_berhasil_transaksi/pengguna_aplikasi
print(f'estimasi proporsi pengguna yang berhasil menyelesaikan transaksi adalah {proporsi_estimasi*100}% \n')

'''Soal 3 - Estimasi Varians
Waktu eksekusi suatu program (ms) dari 6 kali pengujian adalah:
20, 22, 18, 24, 26, 20
Hitung:
- A Rata-rata waktu eksekusi.
- B Varians sampel.
- C Interpretasikan hasil varians tersebut.
'''

# A Rata-rata waktu eksekusi.
waktu_eksekusi_program = np.array([20,22,18,24,26,20])
rata_rata2 = np.mean(waktu_eksekusi_program)
print(f'rata rata waktu eksekusi adalah {rata_rata2:.2f}ms\n')

# B Varians sampel.
waktu_eksekusi = waktu_eksekusi_program
variance_estimasion = np.var(waktu_eksekusi, ddof=1)
print(f'varians sampel nya adalah {variance_estimasion:.2f} ms^2\n')

# C Interpretasikan hasil varians tersebut
# kita harus ukur standar deviasi dengan rata rata, karna varians satuannya ms^2 sedangkan rata rata satuannya ms
# jadi varians tidak serta merta bisa di bandingkan langsung dengan rata-rata
# jadi kita cari dulu standar deviasi nya
std = np.std(waktu_eksekusi,ddof=1)
print(f'standar deviasi = {std:.2f} ms')
# kita bandingkan standar deviasi nya dengan rata rata
# karna standar deviasi(2.94 ms) nya relatif kecil dibanding rata ratanya(21.67 ms) 
# maka sebaran data nya cenderung tidak menyebar
# kita hitung berapa persen simpangan baku dari rata-rata (koefisien variasi)
koefisien_variasi = std / rata_rata2 * 100
print(f'koefisien variasi = {koefisien_variasi:.2f}%\n')

# Interpretasi akhir
print(f'Interpretasi: varians sampel sebesar {variance_estimasion:.2f} ms^2 artinya data waktu eksekusi '
      f'cenderung rapat di sekitar rata-ratanya ({rata_rata2:.2f} ms). Simpangan baku {std:.2f} ms '
      f'hanya sekitar {koefisien_variasi:.2f}% dari rata-rata, sehingga waktu eksekusi program ini '
      f'tergolong konsisten.\n')

'''Soal 4 - Perbedaan Dua Mean
Dua algoritma machine learning diuji untuk mengetahui waktu pelatihan (training time).
Keterangan               | Random Forest | Decision Tree
Jumlah pengujian         | 15            | 15
Rata-rata waktu training | 12 detik      | 5 detik
Hitung estimasi perbedaan rata-rata waktu training kedua algoritma dan jelaskan
algoritma mana yang lebih cepat berdasarkan hasil pengujian.
'''

# Estimasi perbedaan dua mean
jumlah_pengujian = 15
rata_rata_rf = 12   # detik, Random Forest
rata_rata_dt = 5    # detik, Decision Tree
perbedaan_mean = rata_rata_rf - rata_rata_dt
print(f'Estimasi perbedaan rata-rata waktu training (Random Forest - Decision Tree) adalah {perbedaan_mean} detik')

# Algoritma yang lebih cepat adalah yang waktu trainingnya lebih kecil
if perbedaan_mean > 0:
    print(f'Decision Tree lebih cepat {perbedaan_mean} detik dibandingkan Random Forest '
          f'berdasarkan {jumlah_pengujian} kali pengujian pada masing-masing algoritma.')
elif perbedaan_mean < 0:
    print(f'Random Forest lebih cepat {abs(perbedaan_mean)} detik dibandingkan Decision Tree '
          f'berdasarkan {jumlah_pengujian} kali pengujian pada masing-masing algoritma.')
else:
    print('Kedua algoritma memiliki rata-rata waktu training yang sama.')