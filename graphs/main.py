import matplotlib.pyplot as plt
import numpy as np

# Données pour trois séries différentes
x1, y1, sizes1, labels1 = [3.88, 8.63], [4.40, 14.95], [256, 256], ['ChaCha20','ChaCha20-Poly1305']
x2, y2, sizes2, labels2 = [33.57, 39.71, 45.83, 50.90, 60.89, 70.85], [57.53, 68.72, 79.30, 64.99, 77.87, 90.13], [128, 192, 256, 128, 192, 256],\
                          ['AES-128-Encryption ', 'AES-192-Encryption ', 'AES-256-Encryption ', 'AES-128-Decryption', 'AES-192-Decryption', 'AES-256-Decryption ']
x3, y3, sizes3, labels3 = [33.72, 39.86, 45.98, 51.05, 61.04, 71.00], [57.82, 69.02, 79.60, 65.24, 78.13, 90.38], [128, 192, 256, 128, 192, 256],\
                          ['AES-CBC-128-Encryption ', 'AES-CBC-192-Encryption ', 'AES-CBC-256-Encryption ', 'AES-CBC-128-Decryption', 'AES-CBC-192-Decryption', 'AES-CBC-256-Decryption ']
x4, y4, sizes4, labels4 = [33.77, 39.91, 46.03], [58.15, 69.33, 79.91], [128, 192, 256],\
                          ['AES-CTR-128 ', 'AES-CTR-192', 'AES-CTR-256 ']
x5, y5, sizes5, labels5 = [76.57, 82.25, 89.37], [113.02, 124.83, 136.24], [128, 192, 256],\
                          ['AES-GCM-128 ', 'AES-GCM-192', 'AES-GCM-256 ']
x6, y6, sizes6, labels6 = [25.28, 25.55, 16.06, 15.63], [34.26, 34.04, 22.10, 20.18], [128, 128, 128, 128],\
                          ['ASCON-128-Encryption ', 'ASCON-128-Decryption ', 'ASCON-128a-Encryption', 'ASCON-128a-Decryption']

size_factor = 3  # Facteur de multiplication pour augmenter la taille des bulles
sizes1 = [size * size_factor for size in sizes1]
sizes2 = [size * size_factor for size in sizes2]
sizes3 = [size * size_factor for size in sizes3]
sizes4 = [size * size_factor for size in sizes4]
sizes5 = [size * size_factor for size in sizes5]
sizes6 = [size * size_factor for size in sizes6]


# Création du graphique à bulles avec des séries distinctes
plt.figure(figsize=(8, 6))

plt.scatter(x1, y1, s=sizes1, alpha=0.75, edgecolors="k", label=" ChaCha20", color='blue')
plt.scatter(x2, y2, s=sizes2, alpha=0.75, edgecolors="k", label=" AES-ECB", color='#93c47d')
plt.scatter(x3, y3, s=sizes3, alpha=0.75, edgecolors="k", label=" AES-CBC", color='#e9ecb2')#e9ecb2
plt.scatter(x4, y4, s=sizes4, alpha=0.75, edgecolors="k", label=" AES-CTR", color='#f8b96b')#FF5733
plt.scatter(x5, y5, s=sizes5, alpha=0.75, edgecolors="k", label=" AES-GCM", color='red')
plt.scatter(x6, y6, s=sizes6, alpha=0.75, edgecolors="k", label=" ASCON", color='#87cfd1')

# Ajouter les labels pour chaque point
for x, y, label in zip(x1 + x2 + [x6[1]] + [x6[3]], y1 + y2 + [y6[1]] + [y6[3]], labels1 + labels2 + [labels6[1], labels6[3]]):
    plt.text(x+2, y, label, fontsize=6, ha='left', va='top', fontweight='bold')
for x, y, label in zip(x3+[x6[0], x6[2]], y3+[y6[0], y6[2]], labels3+[labels6[0], labels6[2]]):
    plt.text(x+2.5, y+1, label, fontsize=6, ha='left', va='center', fontweight='bold')
for x, y, label in zip(x4+x5, y4+y5, labels4+labels5):
    plt.text(x-2, y, label, fontsize=6, ha='right', va='center', fontweight='bold')

# Création d'une légende pour la taille des bulles
legend_sizes = [size_factor*128, size_factor*192, size_factor*256]
for size in legend_sizes:
    plt.scatter([], [], s=size, alpha=0.6, edgecolors="k", facecolor='none', label=f" Taille de clé: {size//size_factor} bits")

plt.xlabel("Instructions/bit")
plt.ylabel("Cycles/bit")
plt.title("RISCV Benchmark")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), scatterpoints=1, frameon=False, title="Légende", fontsize=8, labelspacing=2.5)
plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)


# Affichage du graphique
plt.tight_layout()
plt.show()

