import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Données pour trois séries différentes
x1, y1, sizes1, labels1 = [3.87, 6.09], [4.40, 7.34], [256, 256], ['ChaCha20', 'ChaCha20-Poly1305']
x2, y2, sizes2, labels2 = [33.56, 39.70, 45.81, 50.88, 60.87, 70.83], [57.46, 68.68, 79.27, 64.93, 77.86, 90.07], [128, 192, 256, 128, 192, 256], \
                          ['AES-128-Enc. ', 'AES-192-Enc. ', 'AES-256-Enc. ', 'AES-128-Dec.', 'AES-192-Dec.', 'AES-256-Dec. ']
x3, y3, sizes3, labels3 = [33.69, 39.83, 45.95, 51.03, 61.01, 70.97], [57.74, 68.93, 79.53, 65.19, 78.08, 90.32], [128, 192, 256, 128, 192, 256], \
                          ['AES-CBC-128-Enc. ', 'AES-CBC-192-Enc. ', 'AES-CBC-256-Enc. ', 'AES-CBC-128-Dec.', 'AES-CBC-192-Dec.', 'AES-CBC-256-Dec. ']
x4, y4, sizes4, labels4 = [33.75, 39.89, 46.00], [57.90, 69.10, 79.70], [128, 192, 256], \
                          ['AES-CTR-128 ', 'AES-CTR-192', 'AES-CTR-256 ']
x5, y5, sizes5, labels5 = [65.89, 70.69, 76.72], [96.61, 106.59, 116.23], [128, 192, 256], \
                          ['AES-GCM-128 ', 'AES-GCM-192', 'AES-GCM-256 ']
x6, y6, sizes6, labels6 = [14.93, 14.87, 10.31, 9.24], [17.13, 16.93, 14.94, 10.33], [128, 128, 128, 128], \
                          ['ASCON-128-Enc. ', 'ASCON-128-Dec. ', 'ASCON-128a-Enc.', 'ASCON-128a-Dec.']

size_factor = 3  # Facteur de multiplication pour augmenter la taille des bulles
sizes1 = [size * size_factor for size in sizes1]
sizes2 = [size * size_factor for size in sizes2]
sizes3 = [size * size_factor for size in sizes3]
sizes4 = [size * size_factor for size in sizes4]
sizes5 = [size * size_factor for size in sizes5]
sizes6 = [size * size_factor for size in sizes6]

# Création du graphique à bulles avec des séries distinctes
plt.figure(figsize=(12, 7))

plt.scatter(x1, y1, s=sizes1, alpha=0.75, edgecolors="k", label=" ChaCha20", color='blue')
plt.scatter(x2, y2, s=sizes2, alpha=0.75, edgecolors="k", label=" AES-ECB", color='#93c47d')
plt.scatter(x3, y3, s=sizes3, alpha=0.75, edgecolors="k", label=" AES-CBC", color='#e9ecb2')  # e9ecb2
plt.scatter(x4, y4, s=sizes4, alpha=0.75, edgecolors="k", label=" AES-CTR", color='#f8b96b')  # FF5733
plt.scatter(x5, y5, s=sizes5, alpha=0.75, edgecolors="k", label=" AES-GCM", color='red')
plt.scatter(x6, y6, s=sizes6, alpha=0.75, edgecolors="k", label=" ASCON", color='#87cfd1')

# Ajouter les labels pour chaque point
for x, y, label in zip(x1 + x2 + [x6[1], x6[3], x6[2]], y1 + y2 + [y6[1], y6[3], y6[2]], labels1 + labels2 + [labels6[1], labels6[3], labels6[2]]):
    plt.text(x + 2, y - 1, label, fontsize=7, ha='left', va='top', fontweight='bold')
for x, y, label in zip(x3 + [x6[0]], y3 + [y6[0]], labels3 + [labels6[0]]):
    plt.text(x + 2.5, y + 1, label, fontsize=7, ha='left', va='center', fontweight='bold')
for x, y, label in zip(x4 + x5, y4 + y5, labels4 + labels5):
    plt.text(x - 2, y, label, fontsize=7, ha='right', va='center', fontweight='bold')

# Création d'une légende pour la taille des bulles
legend_sizes = [size_factor * 128, size_factor * 192, size_factor * 256]
for size in legend_sizes:
    plt.scatter([], [], s=size, alpha=0.6, edgecolors="k", facecolor='none', label=f" Taille de clé: {size // size_factor} bits")

plt.xlabel("Instructions/bit")
plt.ylabel("Cycles/bit")
plt.title("RISCV Benchmark")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), scatterpoints=1, frameon=False, title="Légende", fontsize=9, labelspacing=2.5)
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
        'min_cycles': [22565, 90125, 179805, 225245],  # Cycles minimum
        'max_cycles': [23302, 91678, 182682, 228273],  # Cycles maximum
        'instructions': [19858, 79348, 158668, 198328],
        'block_size': 512,
        'iterations': [50, 100, 500, 1000],
        'delta': [3014, 3520, 3466, 3028],
        'cycles_i_mean': [225361.18, 224845.96, 224793.12, 225248.86],
        'cycles_i_min': [225264, 224776, 224764, 225245],
        'cycles_i_max': [228278, 228296, 228230, 228273],
        'color': '#ec4cb9',
        'style': 0
    },
    'ChaCha20-Poly1305': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [40600.53, 150323.35, 299941.13, 375785.02],
        'min_cycles': [40599, 150298, 299696, 374651],
        'max_cycles': [41514, 152529, 300631, 376736],
        'instructions': [34258, 126826, 250273, 312008],
        'block_size': 512,
        'iterations': [50, 100, 500, 1000],
        'delta': [2028, 2248, 1745, 2085],
        'cycles_i_mean': [375766.08, 375742.43, 375740.49, 375785.02],
        'cycles_i_min': [374574, 374598, 374501, 374651],
        'cycles_i_max': [376602, 376846, 376246, 376736],
        'color': 'pink',
        'style': 0
    },
    'ASCON_128-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [25965.43, 53839.58, 91012.43, 109604.52],
        'min_cycles': [25812, 53674, 90855, 109455],
        'max_cycles': [27985, 55925, 93347, 111977],
        'instructions': [18992, 44522, 78562, 95582],
        'block_size': 64,
        'iterations': [50, 100, 500, 1000],
        'delta': [2458, 2494, 2501, 2522],
        'cycles_i_mean': [109701.24, 109649.21, 109608.94, 109604.52],
        'cycles_i_min': [109514, 109482, 109453, 109455],
        'cycles_i_max': [111972, 111976, 111954, 111977],
        'color': 'blue',
        'style': 0
    },
    'ASCON_128-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [25823.12, 53303.17, 89939.40, 108323.03],
        'min_cycles': [25634, 53167, 89769, 108141],
        'max_cycles': [27462, 55165, 91964, 110334],
        'instructions': [18956, 44366, 78246, 95186],
        'block_size': 64,
        'iterations': [50, 100, 500, 1000],
        'delta': [2239, 2146, 2312, 2193],
        'cycles_i_mean': [108381.22, 108367.46, 108339.59, 108323.03],
        'cycles_i_min': [108209, 108176, 108172, 108141],
        'cycles_i_max': [110448, 110322, 110484, 110334],
        'color': 'blue',
        'style': 1
    },
    'ASCON_128a-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [26986.16, 81765.59, 154732.38, 191212.82],
        'min_cycles': [26860, 81674, 154633, 191106],
        'max_cycles': [28163, 83089, 156255, 192919],
        'instructions': [19469, 56984, 107004, 132013],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [1808, 1790, 1739, 1813],
        'cycles_i_mean': [191306.98, 191285.04, 191266.51, 191212.82],
        'cycles_i_min': [191181, 191158, 191150, 191106],
        'cycles_i_max': [192989, 192948, 192889, 192919],
        'color': 'purple',
        'style': 0
    },
    'ASCON_128a-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [23985.32, 60295.99, 108570.02, 132720.70],
        'min_cycles': [23873, 60142, 108458, 132603],
        'max_cycles': [24946, 61362, 109825, 134202],
        'instructions': [18765, 51915, 96115, 118214],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [1462, 1503, 1575, 1599],
        'cycles_i_mean': [132887.78, 132812.53, 132811.05, 132720.70],
        'cycles_i_min': [132788, 132698, 132686, 132603],
        'cycles_i_max': [134250, 134201, 134261, 134202],
        'color': 'purple',
        'style': 1
    },
    'AES-ECB-128-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [73577.26, 294187.29, 588357.29, 735486.23],
        'min_cycles': [73576, 294186, 588356, 735471],
        'max_cycles': [74127, 294771, 588925, 736151],
        'instructions': [42973, 171813, 343623, 429523],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [680, 683, 680, 680],
        'cycles_i_mean': [735509.56, 735492.14, 735487.46, 735486.23],
        'cycles_i_min': [735471, 735478, 735471, 735471],
        'cycles_i_max': [736151, 736161, 736151, 736151],
        'color': 'brown',
        'style': 0
    },
    'AES-ECB-192-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [87911.19, 351511.28, 703001.31, 878794.1],
        'min_cycles': [87910, 351510, 703000, 878771],
        'max_cycles': [88484, 352091, 703617, 879378],
        'instructions': [50833, 203253, 406503, 508123],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [607, 723, 607, 607],
        'cycles_i_mean': [878815, 878795.86, 878795.2, 878794.1],
        'cycles_i_min': [878771, 878782, 878771, 878771],
        'cycles_i_max': [879378, 879505, 879378, 879378],
        'color': 'brown',
        'style': 1
    },
    'AES-ECB-256-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [101490.12, 405860.11, 811710.13, 1014630.20],
        'min_cycles': [101489, 405859, 811709, 1014629],
        'max_cycles': [102054, 406409, 812275, 1015178],
        'instructions': [58663, 234573, 469143, 586423],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [549, 518, 549, 549],
        'cycles_i_mean': [1014652.98, 1014640.18, 1014631.40, 1014630.20],
        'cycles_i_min': [1014629, 1014629, 1014629, 1014629],
        'cycles_i_max': [1015178, 1015147, 1015178, 1015178],
        'color': 'brown',
        'style': 2
    },
    'AES-ECB-128-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [83148.87, 332436.91, 664861.79, 831099.84],
        'min_cycles': [83148, 332436, 664861, 831099],
        'max_cycles': [83691, 333054, 665383, 831693],
        'instructions': [65153, 260533, 521064, 651325],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [594, 587, 594, 594],
        'cycles_i_mean': [831115.8, 831076.3, 831100.68, 831099.84],
        'cycles_i_min': [831099, 831068, 831099, 831099],
        'cycles_i_max': [831693, 831655, 831693, 831693],
        'color': 'red',
        'style': 0
    },
    'AES-ECB-192-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [99682.78, 398651.81, 797289.71, 996634.77],
        'min_cycles': [99682, 398651, 797289, 996634],
        'max_cycles': [100240, 399168, 797751, 997138],
        'instructions': [77933, 311653, 623304, 779125],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [504, 515, 504, 504],
        'cycles_i_mean': [996649.46, 996610.22, 996635.55, 996634.77],
        'cycles_i_min': [996634, 996603, 996634, 996634],
        'cycles_i_max': [997138, 997118, 997138, 997138],
        'color': 'red',
        'style': 1
    },
    'AES-ECB-256-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [115327.69, 461133.66, 922286.69, 1152875.67],
        'min_cycles': [115327, 461133, 922286, 1152875],
        'max_cycles': [115800, 461568, 923386, 1153291],
        'instructions': [90683, 362653, 725304, 906625],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [416, 451, 416, 416],
        'cycles_i_mean': [1152888.46, 1152851.15, 1152876.35, 1152875.67],
        'cycles_i_min': [1152875, 1152844, 1152875, 1152875],
        'cycles_i_max': [1153291, 1153295, 1153291, 1153291],
        'color': 'red',
        'style': 2
    },
    'AES-CBC-128-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [73965.81, 296087.66, 591232.62, 739023.81],
        'min_cycles': [73964, 296014, 591230, 739021],
        'max_cycles': [74808, 297170, 592769, 740761],
        'instructions': [43160, 172535, 345035, 431285],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [1824, 1782, 1824, 1740],
        'cycles_i_mean': [739076.86, 739049.37, 739025.69, 739023.81],
        'cycles_i_min': [739020, 739020, 739020, 739021],
        'cycles_i_max': [740844, 740802, 740844, 740761],
        'color': 'orange',
        'style': 0
    },
    'AES-CBC-192-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [88294.98, 353465.66, 705875.97, 882322.00],
        'min_cycles': [88293, 353375, 705874, 882320],
        'max_cycles': [89233, 354377, 706880, 883303],
        'instructions': [51020, 203975, 407915, 509885],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [885, 952, 885, 983],
        'cycles_i_mean': [882356.24, 882338.82, 882322.72, 882322.00],
        'cycles_i_min': [882319, 882319, 882319, 882320],
        'cycles_i_max': [883204, 883271, 883204, 883303],
        'color': 'orange',
        'style': 1
    },
    'AES-CBC-256-Encrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [101858.69, 407795.39, 814424.74, 1018015.76],
        'min_cycles': [101857, 407738, 814423, 1018014],
        'max_cycles': [102684, 408634, 815243, 1018945],
        'instructions': [58850, 235295, 470555, 588185],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [864, 827, 864, 931],
        'cycles_i_mean': [1018047.82, 1018031.12, 1018016.48, 1018015.76],
        'cycles_i_min': [1018013, 1018013, 1018013, 1018014],
        'cycles_i_max': [1018877, 1018840, 1018877, 1018945],
        'color': 'orange',
        'style': 2
    },
    'AES-CBC-128-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [83483.23, 334110.09, 667561.26, 834405.21],
        'min_cycles': [83482, 334084, 667560, 834404],
        'max_cycles': [84384, 334972, 668485, 835299],
        'instructions': [65347, 261277, 522517, 653137],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [830, 866, 830, 895],
        'cycles_i_mean': [834427.48, 834415.41, 834405.45, 834405.21],
        'cycles_i_min': [834403, 834403, 834403, 834404],
        'cycles_i_max': [835233, 835269, 835233, 835299],
        'color': 'yellow',
        'style': 0
    },
    'AES-CBC-192-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [99995.12, 400220.42, 799994.97, 999484.90],
        'min_cycles': [99994, 400169, 799994, 999483],
        'max_cycles': [100726, 401080, 800638, 1000609],
        'instructions': [78127, 312397, 624757, 780937],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [1123, 1088, 1123, 1126],
        'cycles_i_mean': [999511.80, 999497.37, 999484.98, 999484.90],
        'cycles_i_min': [999482, 999482, 999482, 999483],
        'cycles_i_max': [1000605, 1000570, 1000605, 1000609],
        'color': 'yellow',
        'style': 1
    },
    'AES-CBC-256-Decrypt': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [115654.96, 463080.77, 924883.91, 1156118.77],
        'min_cycles': [115654, 462995, 924883, 1156118],
        'max_cycles': [116255, 463696, 925477, 1156680],
        'instructions': [90877, 363397, 726757, 908437],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [543, 515, 543, 562],
        'cycles_i_mean': [1156135.72, 1156125.44, 1156118.87, 1156118.77],
        'cycles_i_min': [1156117, 1156117, 1156117, 1156118],
        'cycles_i_max': [1156660, 1156632, 1156660, 1156680],
        'color': 'yellow',
        'style': 2
    },
    'AES-CTR-128': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [74189.16, 296606.57, 592954.13, 741174.23],
        'min_cycles': [74188, 296570, 592953, 741173],
        'max_cycles': [74878, 297416, 593646, 741917],
        'instructions': [43226, 172796, 345556, 431936],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [745, 703, 745, 744],
        'cycles_i_mean': [742013.50, 741951.11, 741992.35, 741174.23],
        'cycles_i_min': [741990, 741940, 741990, 741173],
        'cycles_i_max': [742735, 742643, 742735, 741917],
        'color': '#93c47d',
        'style': 0
    },
    'AES-CTR-192': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [88518.91, 353918.49, 707593.93, 884473.92],
        'min_cycles': [88518, 353890, 707593, 884473],
        'max_cycles': [89010, 354431, 708065, 884945],
        'instructions': [51086, 204236, 408436, 510536],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [495, 499, 495, 470],
        'cycles_i_mean': [885849.78, 885479.04, 885832.88, 884473.92],
        'cycles_i_min': [885831, 885470, 885831, 884473],
        'cycles_i_max': [886326, 885969, 886326, 884945],
        'color': '#93c47d',
        'style': 1
    },
    'AES-CTR-256': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [102088.74, 408211.81, 816153.82, 1020173.82],
        'min_cycles': [102088, 408182, 816153, 1020173],
        'max_cycles': [102460, 408722, 816583, 1020583],
        'instructions': [58916, 235556, 471076, 588836],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [410, 431, 410, 410],
        'cycles_i_mean': [1021700.14, 1021408.54, 1021686.51, 1020173.82],
        'cycles_i_min': [1021685, 1021400, 1021685, 1020173],
        'cycles_i_max': [1022095, 1021831, 1022095, 1020583],
        'color': '#93c47d',
        'style': 2
    },
    'AES-GCM-128': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [157741.43, 517437.62, 996844.35, 1236591.21],
        'min_cycles': [157707, 517382, 996820, 1236552],
        'max_cycles': [158754, 518490, 997996, 1237469],
        'instructions': [109458, 354109, 680308, 843408],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [954, 1074, 954, 917],
        'cycles_i_mean': [1237697.40, 1237556.78, 1237665.96, 1236591.21],
        'cycles_i_min': [1237624, 1237508, 1237624, 1236552],
        'cycles_i_max': [1238578, 1238582, 1238578, 1237469],
        'color': 'green',
        'style': 0
    },
    'AES-GCM-192': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [172328.45, 569739.88, 1099439.72, 1364321.36],
        'min_cycles': [172297, 569686, 1099397, 1364280],
        'max_cycles': [173236, 570677, 1100380, 1365255],
        'instructions': [116190, 379021, 729460, 904680],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [956, 958, 889, 975],
        'cycles_i_mean': [1365934.58, 1365241.55, 1365899.27, 1364321.36],
        'cycles_i_min': [1365865, 1365184, 1365860, 1364280],
        'cycles_i_max': [1366821, 1366142, 1366749, 1365255],
        'color': 'green',
        'style': 1
    },
    'AES-GCM-256': {
        'blocks': [10, 40, 80, 100],
        'mean_cycles': [186528.87, 620378.50, 1198617.03, 1487772.39],
        'min_cycles': [186495, 620316, 1198573, 1487734],
        'max_cycles': [187364, 621244, 1199489, 1488586],
        'instructions': [125226, 410827, 791626, 982026],
        'block_size': 128,
        'iterations': [50, 100, 500, 1000],
        'delta': [872, 879, 838, 852],
        'cycles_i_mean': [1489782.44, 1488978.81, 1489753.82, 1487772.39],
        'cycles_i_min': [1489722, 1488926, 1489708, 1487734],
        'cycles_i_max': [1490594, 1489805, 1490546, 1488586],
        'color': 'green',
        'style': 2
    }
}

for algo, data in algorithms.items():
    block_size = data['block_size']
    blocks = data['blocks']
    mean_cycles = data['mean_cycles']
    instructions = data['instructions']

    data['cycles_per_bit'] = [
        mc / (b * block_size) for mc, b in zip(mean_cycles, blocks)
    ]
    data['instructions_per_bit'] = [
        i / (b * block_size) for i, b in zip(instructions, blocks)
    ]

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

    slope, intercept, r_value, p_value, std_err = linregress(data['blocks'], data['mean_cycles'])
    print(f'{algo_name} fit (R²={r_value ** 2:.2f})')
    print(slope, intercept, r_value, p_value, std_err)
    # Tracer la droite de régression
    y_pred = [slope * xi + intercept for xi in data['blocks']]
    print(y_pred)
    plt.plot(data['blocks'], y_pred, '--', label=f'{algo_name} fit (R²={r_value**2:.2f})', color=data['color'])

plt.xlabel('Nombre de blocs chiffrés')
plt.ylabel('Nombre de cycles')
plt.title('Nombre de cycles par algorithme en fonction du nombre de blocs')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), )

# Utiliser une échelle logarithmique si nécessaire
# plt.xscale('log', base=2)  # Échelle log en base 2 pour l'axe X
# plt.yscale('log', base=2)  # Échelle log en base 2 pour l'axe Y

plt.tight_layout()

# Création du graphique pour les instructions
plt.figure(figsize=(10, 6))
print('')
print('')
# Tracer les lignes pour chaque algorithme
for algo_name, data in algorithms.items():
    plt.plot(data['blocks'], data['instructions'],
             label=algo_name,
             color=data['color'],
             marker=markers[data['style']],
             markersize=4,
             alpha=1,
             linestyle='-',
             linewidth=1)
    slope, intercept, r_value, p_value, std_err = linregress(data['blocks'], data['instructions'])
    print(f'{algo_name} fit (R²={r_value ** 2:.2f})')
    print(slope, intercept, r_value, std_err)

plt.xlabel('Nombre de blocs chiffrés')
plt.ylabel('Nombre d\'instructions')
plt.title('Nombre d\'instructions par algorithme en fonction du nombre de blocs')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Utiliser une échelle logarithmique si nécessaire
plt.xscale('log', base=2)  # Échelle log en base 2 pour l'axe X
plt.yscale('log', base=2)  # Échelle log en base 2 pour l'axe Y

plt.tight_layout()

plt.figure(figsize=(10, 6))

# Tracer les lignes pour chaque algorithme
for algo_name, data in algorithms.items():
    plt.plot(data['blocks'], data['cycles_per_bit'],
             label=algo_name,
             color=data['color'],
             marker=markers[data['style']],
             markersize=4,
             alpha=1,
             linestyle='-',
             linewidth=1)

plt.xlabel('Nombre de blocs chiffrés')
plt.ylabel('Cycles / Bit')
plt.title('Cycles/Bit par algorithme en fonction du nombre de blocs')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Utiliser une échelle logarithmique si nécessaire
# plt.xscale('log', base=2)  # Échelle log en base 2 pour l'axe X
# plt.yscale('log', base=2)  # Échelle log en base 2 pour l'axe Y

plt.tight_layout()

plt.figure(figsize=(10, 6))

# Tracer les lignes pour chaque algorithme
for algo_name, data in algorithms.items():
    plt.plot(data['blocks'], data['instructions_per_bit'],
             label=algo_name,
             color=data['color'],
             marker=markers[data['style']],
             markersize=4,
             alpha=1,
             linestyle='-',
             linewidth=1)

plt.xlabel('Nombre de blocs chiffrés')
plt.ylabel('Instructions / Bit')
plt.title('Instructions/Bit par algorithme en fonction du nombre de blocs')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Utiliser une échelle logarithmique si nécessaire
# plt.xscale('log', base=2)  # Échelle log en base 2 pour l'axe X
# plt.yscale('log', base=2)  # Échelle log en base 2 pour l'axe Y

plt.tight_layout()

plt.figure(figsize=(10, 6))

# Tracer les lignes pour chaque algorithme
for algo_name, data in algorithms.items():
    plt.plot(data['iterations'], data['delta'],
             label=algo_name,
             color=data['color'],
             marker=markers[data['style']],
             markersize=4,
             alpha=1,
             linestyle='-',
             linewidth=1)

plt.xlabel('Nombre d\'itérations')
plt.ylabel('D_cycles')
plt.title('Delta de cycles en fonction du nombre d\'itérations')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Utiliser une échelle logarithmique si nécessaire
# plt.xscale('log', base=2)  # Échelle log en base 2 pour l'axe X
# plt.yscale('log', base=2)  # Échelle log en base 2 pour l'axe Y

plt.tight_layout()

# plt.figure(figsize=(10, 6))
#
# names = ['ChaCha20', 'ChaCha20-Poly1305']
# for algo_name, data in algorithms.items():
#     plt.errorbar(data['iterations'], data['cycles_i_mean'],
#                  yerr=[
#                      [m - min_val for m, min_val in zip(data['cycles_i_mean'], data['cycles_i_min'])],
#                      [max_val - m for m, max_val in zip(data['cycles_i_mean'], data['cycles_i_max'])]
#                  ],
#                  label=algo_name,
#                  color=data['color'],
#                  capsize=5,
#                  capthick=1,
#                  marker=markers[data['style']],
#                  markersize=4,
#                  alpha=1,
#                  linestyle='-',
#                  linewidth=1)
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.tight_layout()
# Création de la figure et des axes (2x2)
fig, axs = plt.subplot_mosaic([['1','2'],['3', '4']], layout='constrained', figsize=(10,6))

# Tracer les mêmes courbes sur chaque subplot (zoom indépendant possible)
for i in ['1', '2', '3', '4']:
    ax = axs[i]
    for algo_name, data in algorithms.items():
        ax.errorbar(  # <<< CHANGÉ ICI : plt.errorbar → ax.errorbar
            data['iterations'], data['cycles_i_mean'],
            yerr=[
                [m - min_val for m, min_val in zip(data['cycles_i_mean'], data['cycles_i_min'])],
                [max_val - m for m, max_val in zip(data['cycles_i_mean'], data['cycles_i_max'])]
            ],
            label=algo_name,
            color=data['color'],
            capsize=5,
            capthick=1,
            marker=markers[data['style']],
            markersize=4,
            alpha=1,
            linestyle='-',
            linewidth=1
        )

# Créer une légende unique à droite
handles, labels = axs['4'].get_legend_handles_labels()
fig.legend(handles, labels, loc='outside right upper', bbox_to_anchor=(1, 0.95))   # Position de la légende
plt.tight_layout(rect=[0, 0, 0.75, 1])

plt.show()
