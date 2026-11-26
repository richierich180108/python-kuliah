"""
412026006 - Richie

Soal di slide tidak memberikan data, jadi data di bawah ini adalah DATA CONTOH
(dummy, dibuat dengan numpy.random seed 42 lalu dibulatkan).
"""

import numpy as np
from scipy import stats
import os
os.system('cls')


def uji_t(judul, data, mu0, alpha, arah, h0, h1, kalimat_tolak, kalimat_gagal):
    """
    Uji-t satu sampel.
    arah: "kanan" (H1: mu > mu0), "kiri" (H1: mu < mu0), "dua" (H1: mu != mu0)
    """
    n = len(data)
    df = n - 1
    mean = np.mean(data)
    sd = np.std(data, ddof=1)  # standar deviasi SAMPEL (dibagi n-1)

    # Statistik uji
    t_hitung = (mean - mu0) / (sd / np.sqrt(n))

    # Nilai kritis (t tabel) dan p-value tergantung arah uji
    if arah == "kanan":
        t_tabel = stats.t.ppf(1 - alpha, df)
        p_value = stats.t.sf(t_hitung, df)
        daerah_tolak = t_hitung > t_tabel
        cek = stats.ttest_1samp(data, mu0, alternative="greater")
    elif arah == "kiri":
        t_tabel = stats.t.ppf(alpha, df)  # nilainya negatif
        p_value = stats.t.cdf(t_hitung, df)
        daerah_tolak = t_hitung < t_tabel
        cek = stats.ttest_1samp(data, mu0, alternative="less")
    else:  # dua arah
        t_tabel = stats.t.ppf(1 - alpha / 2, df)  # batas kritis: ±t_tabel
        p_value = 2 * stats.t.sf(abs(t_hitung), df)
        daerah_tolak = abs(t_hitung) > t_tabel
        cek = stats.ttest_1samp(data, mu0, alternative="two-sided")

    print("=" * 60)
    print(judul)
    print("=" * 60)
    print(f"H0: {h0}")
    print(f"H1: {h1}")
    print(f"level signifikansi = {alpha}, n = {n}, df = {df}, arah uji = {arah}")
    print("-" * 60)
    print("Rata-rata sampel :", round(mean, 4))
    print("Standar deviasi  :", round(sd, 4))
    print("T hitung         :", round(t_hitung, 4))
    if arah == "dua":
        print("T tabel          : ±", round(t_tabel, 4))
    else:
        print("T tabel          :", round(t_tabel, 4))
    print("P-value          :", round(p_value, 4))
    print("-" * 60)

    # Keputusan: pakai p-value (sama seperti di slide), lalu dicek dengan t tabel
    if p_value < alpha:
        print("Keputusan : Tolak H0")
        print("Kesimpulan:", kalimat_tolak)
    else:
        print("Keputusan : Gagal menolak H0")
        print("Kesimpulan:", kalimat_gagal)

    # Pengecekan: dua cara harus memberi keputusan yang sama
    assert (p_value < alpha) == daerah_tolak, "Keputusan p-value dan t tabel beda!"
    # Pengecekan: hasil hitung manual harus sama dengan fungsi bawaan scipy
    assert np.isclose(t_hitung, cek.statistic) and np.isclose(p_value, cek.pvalue)


# ---------------------------------------------------------------
# Soal 1: Latency jaringan -> apakah MELEBIHI 50 ms? (uji kanan)
# ---------------------------------------------------------------
latency = np.array([
    54.8, 46.8, 57.5, 58.6, 41.3, 45.2, 53.8, 51.1, 52.9, 47.9,
    58.3, 57.7, 53.4, 59.8, 55.8, 47.8, 55.2, 47.2, 58.3, 52.7])  # ms, n = 20

uji_t(
    judul="SOAL 1 - Latency jaringan (ms)",
    data=latency, mu0=50, alpha=0.05, arah="kanan",
    h0="mu <= 50", h1="mu > 50",
    kalimat_tolak="Rata-rata latency melebihi 50 ms.",
    kalimat_gagal="Belum ada bukti bahwa rata-rata latency melebihi 50 ms.",
)

# ---------------------------------------------------------------
# Soal 2: F1-score -> apakah BERBEDA dari 0.85? (dua arah)
# ---------------------------------------------------------------
f1 = np.array([
    0.855, 0.843, 0.891, 0.856, 0.849, 0.851, 0.873, 0.869,
    0.870, 0.871, 0.914, 0.850, 0.847, 0.840, 0.875])  # n = 15

uji_t(
    judul="SOAL 2 - F1-score model klasifikasi",
    data=f1, mu0=0.85, alpha=0.05, arah="dua",
    h0="mu = 0.85", h1="mu != 0.85",
    kalimat_tolak="Rata-rata F1-score berbeda dari 0.85.",
    kalimat_gagal="Belum ada bukti bahwa rata-rata F1-score berbeda dari 0.85.",
)

# ---------------------------------------------------------------
# Soal 3: Waktu penyelesaian tugas -> apakah LEBIH KECIL dari 30 detik? (uji kiri)
# ---------------------------------------------------------------
waktu = np.array([
    32.0, 27.0, 24.1, 24.2, 30.1, 30.5, 29.7, 24.8, 28.4, 28.0,
    28.4, 31.0, 28.4, 30.2, 27.8, 28.7, 30.0, 21.7, 26.2, 25.6])  # detik, n = 20

uji_t(
    judul="SOAL 3 - Waktu penyelesaian tugas aplikasi mobile (detik)",
    data=waktu, mu0=30, alpha=0.05, arah="kiri",
    h0="mu >= 30", h1="mu < 30",
    kalimat_tolak="Rata-rata waktu penyelesaian lebih kecil dari 30 detik.",
    kalimat_gagal="Belum ada bukti bahwa rata-rata waktu penyelesaian lebih kecil dari 30 detik.",
)

# ---------------------------------------------------------------
# Soal 4: Waktu query database -> apakah BERBEDA dari 200 ms? (dua arah)
# ---------------------------------------------------------------
query = np.array([
    195.5, 202.0, 233.9, 191.4, 224.4, 176.7, 201.0, 209.9,
    217.6, 219.8, 221.3, 200.7, 198.7, 222.4, 203.6])  # ms, n = 15

uji_t(
    judul="SOAL 4 - Waktu query database (ms)",
    data=query, mu0=200, alpha=0.05, arah="dua",
    h0="mu = 200", h1="mu != 200",
    kalimat_tolak="Rata-rata waktu query berbeda dari 200 ms.",
    kalimat_gagal="Belum ada bukti bahwa rata-rata waktu query berbeda dari 200 ms.",
)