"""
Proyek 2 - Pembuatan Circular Mask
Kuliah 13 Diferensial dan Integral (Substitusi Trigonometri)

Soal:
 (a) Buat lingkaran dengan radius 20, 40, dan 60 piksel.
 (b) Hitung luas menggunakan integral.
 (c) Buat circular mask menggunakan NumPy.
 (d) Bandingkan luas analitik dengan jumlah piksel aktual.
 (e) Tampilkan perbedaan tepi lingkaran dengan dan tanpa anti-aliasing.

Ide matematikanya (sama seperti contoh radius 40 di slide):
    persamaan lingkaran : x^2 + y^2 = r^2  ->  y = sqrt(r^2 - x^2)
    karena simetris     : A = 4 * integral_0^r sqrt(r^2 - x^2) dx
    substitusi          : x = r sin(theta), dx = r cos(theta) dtheta, batas 0 -> pi/2
                        : A = 4 r^2 * integral_0^(pi/2) cos^2(theta) dtheta
                        :   = 4 r^2 * (pi/4) = pi * r^2
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
os.system('cls')

x = sp.symbols("x", real=True)

daftar_radius = [20, 40, 60]   # piksel -> poin (f)


# ---------------------------------------------------------------
# (a) Luas lingkaran lewat integral
# ---------------------------------------------------------------
def luas_integral(r):
    """A = 4 * integral_0^r sqrt(r^2 - x^2) dx  (hasil eksak dari sympy)."""
    return 4 * sp.integrate(sp.sqrt(r**2 - x**2), (x, 0, r))


# ---------------------------------------------------------------
# (b) Circular mask dengan NumPy (tanpa anti-aliasing: nilai 0 atau 1)
# ---------------------------------------------------------------
def buat_koordinat(r):
    """Grid koordinat piksel dari -r sampai r (pusat lingkaran di (0, 0))."""
    sumbu = np.arange(-r, r + 1)
    X, Y = np.meshgrid(sumbu, sumbu)
    return X, Y


def mask_biasa(X, Y, r):
    """True kalau titik pusat piksel berada di dalam lingkaran."""
    return X**2 + Y**2 <= r**2


# ---------------------------------------------------------------
# (c) Mask dengan anti-aliasing (supersampling)
#     Tiap piksel dibagi menjadi k x k sub-piksel. Nilai piksel =
#     persentase sub-piksel yang berada di dalam lingkaran (0.0 - 1.0).
#     Jadi piksel di tepi punya nilai di antara 0 dan 1 -> tepi halus.
# ---------------------------------------------------------------
def mask_antialias(X, Y, r, k=16):
    geser = (np.arange(k) + 0.5) / k - 0.5      # posisi sub-piksel di dalam 1 piksel
    isi = np.zeros(X.shape)
    for dx in geser:
        for dy in geser:
            isi += (X + dx) ** 2 + (Y + dy) ** 2 <= r**2
    return isi / (k * k)


# ---------------------------------------------------------------
# (d) Bandingkan luas analitik dengan jumlah piksel
# ---------------------------------------------------------------
data = {}   # r -> (X, Y, mask biasa, mask anti-alias)

print("=" * 86)
print("PROYEK 2 - perbandingan LUAS ANALITIK dengan JUMLAH PIKSEL")
print("=" * 86)
print(f"{'r (px)':<8}{'A integral':<14}{'A (px^2)':<12}{'Piksel mask':<13}"
      f"{'Selisih':<10}{'Err %':<9}{'Jml AA':<11}{'Selisih AA':<11}")

for r in daftar_radius:
    X, Y = buat_koordinat(r)
    m = mask_biasa(X, Y, r)
    aa = mask_antialias(X, Y, r)
    data[r] = (X, Y, m, aa)

    A_eksak = luas_integral(r)
    A = float(A_eksak)
    jumlah_piksel = int(np.sum(m))
    jumlah_aa = float(np.sum(aa))
    selisih = jumlah_piksel - A
    selisih_aa = jumlah_aa - A
    persen = abs(selisih) / A * 100

    print(f"{r:<8}{str(A_eksak):<14}{A:<12.2f}{jumlah_piksel:<13}"
          f"{selisih:<10.2f}{persen:<9.3f}{jumlah_aa:<11.2f}{selisih_aa:<11.2f}")

print()
print("Keterangan: 'Selisih' = jumlah piksel mask biasa - luas integral.")
print("            'Jml AA'  = jumlah seluruh nilai piksel pada mask anti-aliasing.")

# ---------------------------------------------------------------
# Visualisasi 1: circular mask (tanpa anti-aliasing) untuk tiap radius
# ---------------------------------------------------------------
fig1, sumbu_gambar = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)
for ax, r in zip(sumbu_gambar, daftar_radius):
    X, Y, m, aa = data[r]
    im = ax.imshow(m, extent=[-r - 0.5, r + 0.5, -r - 0.5, r + 0.5],
                   origin="lower", cmap="Blues", interpolation="nearest")
    ax.set_title(f"Circular mask r = {r} px\n"
                 f"piksel = {int(m.sum())},  luas = {np.pi * r**2:.2f}")
    ax.set_xlabel("Koordinat X")
    ax.set_ylabel("Koordinat Y")
fig1.colorbar(im, ax=sumbu_gambar, label="Mask", shrink=0.8)
fig1.savefig("proyek2_mask.png", dpi=150, bbox_inches="tight")

# ---------------------------------------------------------------
# Visualisasi 2: tepi lingkaran tanpa anti-aliasing dengan anti-aliasing (r = 40)
# Baris atas : seluruh lingkaran
# Baris bawah: diperbesar di sekitar tepi (arah 45 derajat)
# ---------------------------------------------------------------
r = 40
X, Y, m, aa = data[r]
batas = [-r - 0.5, r + 0.5, -r - 0.5, r + 0.5]

fig2, ax = plt.subplots(2, 2, figsize=(11, 11))
judul = ["Tanpa anti-aliasing (0 atau 1)", "Dengan anti-aliasing (0.0 - 1.0)"]
for kolom, (gambar, nama) in enumerate(zip([m.astype(float), aa], judul)):
    # baris atas: tampilan penuh
    ax[0, kolom].imshow(gambar, extent=batas, origin="lower", cmap="Blues",
                        interpolation="nearest", vmin=0, vmax=1)
    ax[0, kolom].set_title(nama)
    ax[0, kolom].set_xlabel("Koordinat X")
    ax[0, kolom].set_ylabel("Koordinat Y")

    # baris bawah: zoom ke tepi lingkaran
    ax[1, kolom].imshow(gambar, extent=batas, origin="lower", cmap="Blues",
                        interpolation="nearest", vmin=0, vmax=1)
    ax[1, kolom].set_xlim(22, 34)
    ax[1, kolom].set_ylim(22, 34)
    ax[1, kolom].set_title(nama + " (zoom tepi)")
    ax[1, kolom].set_xlabel("Koordinat X")
    ax[1, kolom].set_ylabel("Koordinat Y")

fig2.suptitle("Perbedaan tepi circular mask, radius 40 piksel", fontsize=11)
fig2.tight_layout()
fig2.savefig("proyek2_antialiasing.png", dpi=150)

plt.show()

#KESIMPULAN

'''
perbandingan antara luas analitik dengan jumlah piksel aktualnya sangat sedikit selisih nya
perbedaan tepi lingkaran menggunakan anti-aliasing dengan tanpa anti-aliasing adalah
dengan anti-aliasing, tepi lingkaran terlihat lebih halus dan peralihan tepinya bertahap (gradiasi)
tanpa anti-aliasing, tepi lingkaran terlihat lebih natural, dan lebih akurat 
'''