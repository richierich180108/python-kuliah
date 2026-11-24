import math
from scipy import stats
import os
os.system('cls')


def ci_mean(xbar, spread, n, conf, pakai_t=False):
    """Confidence interval untuk mean.
    spread = sigma (populasi) kalau pakai Z, atau s (sampel) kalau pakai t.
    """
    alpha = 1 - conf
    if pakai_t:
        kritis = stats.t.ppf(1 - alpha / 2, df=n - 1)
    else:
        kritis = stats.norm.ppf(1 - alpha / 2)
    E = kritis * spread / math.sqrt(n)
    return kritis, E, xbar - E, xbar + E


def cetak(judul, hasil, satuan=""):
    kritis, E, bawah, atas = hasil
    print(judul)
    print(f"  nilai kritis = {kritis:.4f}")
    print(f"  margin error = {E:.4f} {satuan}")
    print(f"  interval     = {bawah:.4f} <= μ <= {atas:.4f} {satuan}\n")


# SOAL 1: n=144, xbar=20000, sigma=6000 (diketahui) -> Z
cetak("SOAL 1a (99%)", ci_mean(20_000, 6_000, 144, 0.99), "rupiah")
cetak("SOAL 1b (90%)", ci_mean(20_000, 6_000, 144, 0.90), "rupiah")
print('SOAL 1c Interpretasi \ndengan tingkat keyakinan 99%, rata-rata pengeluaran per hari seluruh karyawan diduga berada di antara Rp18.712 dan Rp21.288. Kalau pengambilan sampel diulang banyak kali, sekitar 99% interval yang terbentuk akan memuat μ yang sebenarnya. Interval 90% lebih sempit tetapi keyakinannya lebih rendah. Jadi ada pertukaran antara keyakinan dan presisi.\n')

# SOAL 2: n=100, xbar=9600, s=160, n >= 30 -> Z 
cetak("SOAL 2 (98%, Z)", ci_mean(9_600, 160, 100, 0.98), "rupiah")
cetak("SOAL 2 (98%, t, pembanding)", ci_mean(9_600, 160, 100, 0.98, pakai_t=True), "rupiah")

# SOAL 3: n=60, xbar=7.72, sigma=0.73 (diketahui) -> Z
cetak("SOAL 3 (95%)", ci_mean(7.72, 0.73, 60, 0.95), "%")

# SOAL 4: n=25, xbar=20, s=8, n < 30 -> t
cetak("SOAL 4 (99%, t)", ci_mean(20, 8, 25, 0.99, pakai_t=True), "%")
cetak("SOAL 4 (99%, Z, pembanding)", ci_mean(20, 8, 25, 0.99), "%")