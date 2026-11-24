# ==========================================================
# Kuliah 13 - Latihan Confidence Interval (estimasi interval) untuk mean
# ==========================================================
# Bentuk umum interval kepercayaan untuk mean populasi (μ):
#       X̄ - E  <=  μ  <=  X̄ + E
# dengan margin error:
#       E = nilai_kritis * (simpangan_baku / akar(n))
#
# Memilih nilai kritis:
#   - Z (distribusi normal)   -> σ populasi diketahui, atau n >= 30 (aturan slide 18)
#   - t (distribusi Student)  -> σ tidak diketahui dan n < 30, dengan df = n - 1
# ==========================================================

import math                  # untuk akar kuadrat: math.sqrt()
from scipy import stats      # untuk mencari nilai Z dan t (pengganti membaca tabel)
import os                    # untuk membersihkan layar terminal
os.system('cls')             # 'cls' = clear screen di Windows (di Mac/Linux pakai 'clear')


def ci_mean(xbar, sebaran, n, conf, pakai_t=False):
    """Menghitung confidence interval untuk mean.

    xbar    : rata-rata sampel (X̄)
    sebaran : sigma (populasi) kalau pakai Z, atau s (sampel) kalau pakai t
    n       : jumlah sampel
    conf    : tingkat keyakinan dalam desimal (99% -> 0.99)
    pakai_t : False = pakai Z (normal), True = pakai t

    Mengembalikan 4 nilai: nilai kritis, margin error, batas bawah, batas atas.
    """
    # alpha = peluang "meleset". Keyakinan 95% -> alpha = 0.05
    alpha = 1 - conf

    if pakai_t:
        # ppf = kebalikan tabel: kita masukkan luas area, hasilnya nilai kritis.
        # Dipakai 1 - alpha/2 karena alpha dibagi dua ekor (kiri dan kanan).
        # df (derajat kebebasan) = n - 1
        kritis = stats.t.ppf(1 - alpha / 2, df=n - 1)
    else:
        # Sama seperti di atas, tapi dari distribusi normal baku (Z), tanpa df
        kritis = stats.norm.ppf(1 - alpha / 2)

    # Margin error: E = nilai kritis * sebaran / akar(n)
    E = kritis * sebaran / math.sqrt(n)

    # Batas bawah = X̄ - E, batas atas = X̄ + E
    return kritis, E, xbar - E, xbar + E


def cetak(judul, hasil, satuan=""):
    # 'hasil' berisi 4 nilai dari ci_mean, dibongkar ke 4 variabel sekaligus
    kritis, E, bawah, atas = hasil
    print(judul)
    # :.4f artinya tampilkan 4 angka di belakang koma
    print(f"  nilai kritis = {kritis:.4f}")
    print(f"  margin error = {E:.4f} {satuan}")
    print(f"  interval     = {bawah:.4f} <= μ <= {atas:.4f} {satuan}\n")


# ----------------------------------------------------------
# SOAL 1: n=144, X̄=20000, σ=6000 (σ populasi diketahui) -> pakai Z
# Diminta: CI 99% dan 90%, lalu interpretasi
# (angka 20_000 sama dengan 20000, garis bawah hanya supaya mudah dibaca)
# ----------------------------------------------------------
cetak("SOAL 1a (99%)", ci_mean(20_000, 6_000, 144, 0.99), "rupiah")
cetak("SOAL 1b (90%)", ci_mean(20_000, 6_000, 144, 0.90), "rupiah")
print('SOAL 1c Interpretasi \ndengan tingkat keyakinan 99%, rata-rata pengeluaran per hari seluruh karyawan diduga berada di antara Rp18.712 dan Rp21.288. Kalau pengambilan sampel diulang banyak kali, sekitar 99% interval yang terbentuk akan memuat μ yang sebenarnya. Interval 90% lebih sempit tetapi keyakinannya lebih rendah. Jadi ada pertukaran antara keyakinan dan presisi.\n')

# ----------------------------------------------------------
# SOAL 2: n=100, X̄=9600, s=160 (simpangan baku sampel)
# σ tidak diketahui, tapi n >= 30 -> pakai Z (aturan slide 18)
# Baris kedua memakai t hanya sebagai pembanding: hasilnya sedikit lebih lebar
# ----------------------------------------------------------
cetak("SOAL 2 (98%, Z)", ci_mean(9_600, 160, 100, 0.98), "rupiah")
cetak("SOAL 2 (98%, t, pembanding)", ci_mean(9_600, 160, 100, 0.98, pakai_t=True), "rupiah")

# ----------------------------------------------------------
# SOAL 3: n=60, X̄=7.72, σ=0.73 (σ populasi diketahui) -> pakai Z
# Satuannya persen, jadi hasil interval juga dalam persen
# ----------------------------------------------------------
cetak("SOAL 3 (95%)", ci_mean(7.72, 0.73, 60, 0.95), "%")

# ----------------------------------------------------------
# SOAL 4: n=25, X̄=20, s=8 (dianggap simpangan baku sampel)
# n < 30 dan σ tidak diketahui -> pakai t (df = 24)
# Baris kedua memakai Z hanya sebagai pembanding (kalau 8% dianggap σ populasi)
# ----------------------------------------------------------
cetak("SOAL 4 (99%, t)", ci_mean(20, 8, 25, 0.99, pakai_t=True), "%")
cetak("SOAL 4 (99%, Z, pembanding)", ci_mean(20, 8, 25, 0.99), "%")