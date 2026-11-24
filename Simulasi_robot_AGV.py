"""
Proyek 1 - Simulasi Robot AGV
Kuliah 13 Diferensial dan Integral (Substitusi Trigonometri)

Soal:
 (a) Buat lintasan berbentuk seperempat lingkaran.
 (b) Hitung panjang lintasan menggunakan integral.
 (c) Ubah radius menjadi 2, 3, 4, dan 5 meter.
 (d) Bandingkan waktu perjalanan pada kecepatan berbeda.
 (e) Visualisasikan lintasan menggunakan Matplotlib.

Ide matematikanya (sama seperti contoh radius 2 di slide):
    lintasan   : y = sqrt(r^2 - x^2),  0 <= x <= r
    turunan    : dy/dx = -x / sqrt(r^2 - x^2)
    panjang    : L = integral_0^r sqrt(1 + (dy/dx)^2) dx
               = integral_0^r r / sqrt(r^2 - x^2) dx
    substitusi : x = r sin(theta), dx = r cos(theta) dtheta, batas 0 -> pi/2
               = integral_0^(pi/2) r dtheta = r * pi / 2
    waktu      : t = L / v
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
os.system('cls')

x = sp.symbols("x", real=True)

# ---------------------------------------------------------------
# Data masukan
# ---------------------------------------------------------------
daftar_radius = [2, 3, 4, 5]             # meter  -> poin (c)
daftar_kecepatan = [0.5, 1.0, 1.5, 2.0]  # m/detik -> poin (d)


# ---------------------------------------------------------------
# (a) dan (b) Model lintasan dan panjang lintasan lewat integral
# ---------------------------------------------------------------
def panjang_lintasan(r):
    """Panjang seperempat lingkaran radius r (hasil eksak dari sympy)."""
    y = sp.sqrt(r**2 - x**2)              # (a) lintasan seperempat lingkaran
    dy = sp.diff(y, x)                    # turunan
    integrand = sp.sqrt(1 + dy**2)        # rumus panjang kurva
    return sp.integrate(integrand, (x, 0, r))   # (b) integral tentu


# ---------------------------------------------------------------
# (c) Hitung untuk semua radius
# ---------------------------------------------------------------
hasil = {}   # r -> panjang lintasan (angka desimal)

print("=" * 62)
print("PROYEK 1 - PANJANG LINTASAN ROBOT AGV")
print("=" * 62)
print(f"{'Radius (m)':<12}{'L eksak':<12}{'L numerik (m)':<16}{'Cek pi*r/2':<12}")
for r in daftar_radius:
    L_eksak = panjang_lintasan(r)
    L_num = float(L_eksak)
    pembanding = np.pi * r / 2            # 1/4 keliling lingkaran
    hasil[r] = L_num
    print(f"{r:<12}{str(L_eksak):<12}{L_num:<16.4f}{pembanding:<12.4f}")

# ---------------------------------------------------------------
# (d) Bandingkan waktu perjalanan pada kecepatan berbeda: t = L / v
# ---------------------------------------------------------------
print()
print("WAKTU PERJALANAN (detik) = L / v")
kepala = f"{'Radius (m)':<12}" + "".join(f"v={v} m/s".ljust(14) for v in daftar_kecepatan)
print(kepala)
for r in daftar_radius:
    baris = f"{r:<12}"
    for v in daftar_kecepatan:
        waktu = hasil[r] / v
        baris += f"{waktu:<14.3f}"
    print(baris)

print()

# ---------------------------------------------------------------
# (e) Visualisasi dengan Matplotlib
# ---------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# --- Panel kiri: lintasan seperempat lingkaran untuk tiap radius ---
for r in daftar_radius:
    xx = np.linspace(0, r, 300)
    yy = np.sqrt(r**2 - xx**2)
    garis, = ax1.plot(xx, yy, linewidth=2.5, label=f"r = {r} m  (L = {hasil[r]:.2f} m)")
    # titik awal A = (0, r) dan titik akhir B = (r, 0)
    ax1.scatter([0, r], [r, 0], color=garis.get_color(), zorder=3)

ax1.set_xlabel("Posisi X (meter)")
ax1.set_ylabel("Posisi Y (meter)")
ax1.set_title("Lintasan robot AGV: seperempat lingkaran")
ax1.axis("equal")
ax1.grid(True)
ax1.legend()

# --- Panel kanan: waktu tempuh vs kecepatan ---
for r in daftar_radius:
    waktu = [hasil[r] / v for v in daftar_kecepatan]
    ax2.plot(daftar_kecepatan, waktu, marker="o", linewidth=2, label=f"r = {r} m")

ax2.set_xlabel("Kecepatan robot (m/detik)")
ax2.set_ylabel("Waktu tempuh (detik)")
ax2.set_title("Waktu tempuh = L / v")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("proyek1_hasil.png", dpi=150)
plt.show()

#KESIMPULAN
'''
Semakin besar kecepatannya maka, waktu perjalanan nya makin pendek
semakin besar radius maka, semakin besar juga panjang lintasan dan waktu perjalanannya 
'''