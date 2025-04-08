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

# Création d'un deuxième graphique
plt.figure(figsize=(10, 6))

# Exemple de données (à remplacer par vos vraies données)
# Format: [nombre_de_blocs, cycles_moyens, cycles_min, cycles_max]

algorithms = {
    'ChaCha20': {
        'blocks': [10, 40, 80, 100],  # Nombre de blocs
        'mean_cycles': [22566.01, 90126.86, 179808.89, 225248.86],  # Cycles moyens
        'min_cycles': [22565, 90125, 179805, 225245],    # Cycles minimum
        'max_cycles': [23302, 91678, 182682, 228273],    # Cycles maximum
        'instructions': [19858, 79348, 158668, 198328],
        'color': '#ec4cb9',
        'style': 0
    },
    'ChaCha20-Poly1305': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [40600.53, 150323.35, 299941.13, 375785.02],
        'min_cycles': [40599, 150298, 299696, 374651],
        'max_cycles': [41514, 152529, 300631, 376736],
        'instructions': [34258, 126826, 250273, 312008],
        'color': 'pink',
        'style': 0
    },
    'ASCON_128-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [25965.43, 53839.58, 91012.43, 109604.52],
        'min_cycles': [25812, 53674, 90855, 109455],
        'max_cycles': [27985, 55925, 93347, 111977],
        'instructions': [18992, 44522, 78562, 429523],
        'color': 'blue',
        'style': 0
    },
    'ASCON_128-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [25823.12, 53303.17, 89939.40, 108323.03],
        'min_cycles': [25634, 53167, 89769, 108141],
        'max_cycles': [27462, 55165, 91964, 110334],
        'instructions': [18956, 44366, 91964, 0],
        'color': 'blue',
        'style': 1
    },
    'ASCON_128a-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [26986.16, 81765.59, 154732.38, 191212.82],
        'min_cycles': [26860, 81674, 154633, 191106],
        'max_cycles': [28163, 83089, 156255, 192919],
        'instructions': [19469, 56984, 107004, 0],
        'color': 'purple',
        'style': 0
    },
    'ASCON_128a-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [23985.32, 60295.99, 108570.02, 132720.70],
        'min_cycles': [23873, 60142, 108458, 132603],
        'max_cycles': [24946, 61362, 109825, 134202],
        'instructions': [18765, 51915, 96115, 0],
        'color': 'purple',
        'style': 1
    },
    'AES-ECB-128-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [73577.26, 294187.29, 588357.29, 735486.23],
        'min_cycles': [73576, 294186, 588356, 735471],
        'max_cycles': [74127, 294771, 588925, 736151],
        'instructions': [42973, 171813, 343623, 0],
        'color': 'brown',
        'style': 0
    },
    'AES-ECB-192-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [87911.19, 351511.28, 703001.31, 878794.1],
        'min_cycles': [87910, 351510, 703000, 878771],
        'max_cycles': [88484, 352091, 703617, 879378],
        'instructions': [50833, 203253, 406503, 0],
        'color': 'brown',
        'style': 1
    },
    'AES-ECB-256-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [101490.12, 405860.11, 811710.13, 1014630.20],
        'min_cycles': [101489, 405859, 811709, 1014629],
        'max_cycles': [102054, 406409, 812275, 1015178],
        'instructions': [58663, 234573, 469143, 0],
        'color': 'brown',
        'style': 2
    },
    'AES-ECB-128-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [83148.87, 332436.91, 664861.79, 831099.84],
        'min_cycles': [83148, 332436, 664861, 831099],
        'max_cycles': [83691, 333054, 665383, 831693],
        'instructions': [65153, 260533, 588908, 0],
        'color': 'red',
        'style': 0
    },
    'AES-ECB-192-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [99682.78, 398651.81, 797289.71, 996634.77],
        'min_cycles': [99682, 398651, 797289, 996634],
        'max_cycles': [100240, 399168, 797751, 997138],
        'instructions': [77933, 311653, 623304, 0],
        'color': 'red',
        'style': 1
    },
    'AES-ECB-256-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [115327.69, 461133.66, 922286.69, 1152875.67],
        'min_cycles': [115327, 461133, 922286, 1152875],
        'max_cycles': [115800, 461568, 923386, 1153291],
        'instructions': [90683, 362653, 725304, 0],
        'color': 'red',
        'style': 2
    },
    'AES-CBC-128-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [73965.81, 296087.66, 591232.62, 739023.81],
        'min_cycles': [73964, 296014, 591230, 739021],
        'max_cycles': [74808, 297170, 592769, 740761],
        'instructions': [43160, 172535, 345035, 0],
        'color': 'orange',
        'style': 0
    },
    'AES-CBC-192-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [88294.98, 353465.66, 705875.97, 882322.00],
        'min_cycles': [88293, 353375, 705874, 882320],
        'max_cycles': [89233, 354377, 706880, 883303],
        'instructions': [51020, 203975, 407915, 0],
        'color': 'orange',
        'style': 1
    },
    'AES-CBC-256-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [101858.69, 407795.39, 814424.74, 1018015.76],
        'min_cycles': [101857, 407738, 814423, 1018014],
        'max_cycles': [102684, 408634, 815243, 1018945],
        'instructions': [58850, 235295, 470555, 0],
        'color': 'orange',
        'style': 2
    },
    'AES-CBC-128-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [83483.23, 334110.09, 667561.26, 834405.21],
        'min_cycles': [83482, 334084, 667560, 834404],
        'max_cycles': [84384, 334972, 668485, 835299],
        'instructions': [65347, 261277, 522517, 0],
        'color': 'yellow',
        'style': 0
    },
    'AES-CBC-192-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [99995.12, 400220.42, 799994.97, 999484.90],
        'min_cycles': [99994, 400169, 799994, 999483],
        'max_cycles': [100726, 401080, 800638, 1000609],
        'instructions': [78127, 312397, 624757, 0],
        'color': 'yellow',
        'style': 1
    },
    'AES-CBC-256-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [115654.96, 463080.77, 924883.91, 1156118.77],
        'min_cycles': [115654, 462995, 924883, 1156118],
        'max_cycles': [116255, 463696, 925477, 1156680],
        'instructions': [90877, 363397, 726757, 0],
        'color': 'yellow',
        'style': 2
    },
    'AES-CTR-128': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [74189.16, 296606.57, 592954.13, 741174.23],
        'min_cycles': [74188, 296570, 592953, 741173],
        'max_cycles': [74878, 297416, 593646, 741917],
        'instructions': [43226, 172796, 345556, 0],
        'color': '#93c47d',
        'style': 0
    },
    'AES-CTR-192': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [88518.91, 353918.49, 707593.93, 884473.92],
        'min_cycles': [88518, 353890, 707593, 884473],
        'max_cycles': [89010, 354431, 708065, 884945],
        'instructions': [51086, 204236, 408436, 0],
        'color': '#93c47d',
        'style': 1
    },
    'AES-CTR-256': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [102088.74, 408211.81, 816153.82, 1020173.82],
        'min_cycles': [102088, 408182, 816153, 1020173],
        'max_cycles': [102460, 408722, 816583, 1020583],
        'instructions': [58916, 235556, 471076, 0],
        'color': '#93c47d',
        'style': 2
    },
    'AES-GCM-128': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [157741.43, 517437.62, 996844.35, 1236591.21],
        'min_cycles': [157707, 517382, 996820, 1236552],
        'max_cycles': [158754, 518490, 997996, 1237469],
        'instructions': [109458, 354109, 680308, 0],
        'color': 'green',
        'style': 0
    },
    'AES-GCM-192': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [172328.45, 569739.88, 1099439.72, 1364321.36],
        'min_cycles': [172297, 569686, 1099397, 1364280],
        'max_cycles': [173236, 570677, 1100380, 1365255],
        'instructions': [116190, 379021, 729460, 0],
        'color': 'green',
        'style': 1
    },
    'AES-GCM-256': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [186528.87, 620378.50, 1198617.03, 1487772.39],
        'min_cycles': [186495, 620316, 1198573, 1487734],
        'max_cycles': [187364, 621244, 1199489, 1488586],
        'instructions': [125226, 410827, 791626, 0],
        'color': 'green',
        'style': 2
    }
}

markers = ['o', 's', 'D', '^', 'v', '<', '>']

# Tracer les lignes avec barres d'erreur pour chaque algorithme
for algo_name, data in algorithms.items():
    plt.errorbar(data['blocks'], data['mean_cycles'],
                yerr=[
                    [m - min_val for m, min_val in zip(data['mean_cycles'], data['min_cycles'])],
                    [max_val - m for m, max_val in zip(data['mean_cycles'], data['max_cycles'])]
                ],
                label=algo_name,
                color=data['color'],
                capsize=5,
                capthick=1,
                marker=markers[data['style']],
                markersize=4,
                alpha=1,
                linestyle='-',
                linewidth=1)


plt.xlabel('Nombre de blocs chiffrés')
plt.ylabel('Nombre de cycles')
plt.title('Performance des algorithmes en fonction du nombre de blocs')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1),)

# Utiliser une échelle logarithmique si nécessaire
#plt.xscale('log', base=2)  # Échelle log en base 2 pour l'axe X
#plt.yscale('log', base=2)  # Échelle log en base 2 pour l'axe Y

plt.tight_layout()
plt.show()

