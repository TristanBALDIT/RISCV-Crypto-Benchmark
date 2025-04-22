import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
from data import *

##############################################################################################
#                                       DISPLAY CHOICES                                     #
##############################################################################################

plot_bubbles = False

plot_cycles_per_blocks = True
log_cycles_per_blocks = False

plot_instructions_per_blocks = True
log_instructions_per_blocks = False

plot_cycles_per_bit_per_blocks = True
plot_instructions_per_bit_per_blocks = True

plot_delta = False
plot_cycles_per_iteration = False

plot_cycles_per_ad = True
plot_instructions_per_ad = True

##############################################################################################
#                                       PLOTS CODE                                           #
##############################################################################################

# data transformation
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


#Bubble plot
if plot_bubbles:
    size_factor = 3  # Size factor for bubbles
    sizes1 = [size * size_factor for size in sizes1]
    sizes2 = [size * size_factor for size in sizes2]
    sizes3 = [size * size_factor for size in sizes3]
    sizes4 = [size * size_factor for size in sizes4]
    sizes5 = [size * size_factor for size in sizes5]
    sizes6 = [size * size_factor for size in sizes6]

    # Graph creation
    plt.figure(figsize=(12, 7))

    plt.scatter(x1, y1, s=sizes1, alpha=0.75, edgecolors="k", label=" ChaCha20", color='blue')
    plt.scatter(x2, y2, s=sizes2, alpha=0.75, edgecolors="k", label=" AES-ECB", color='#93c47d')
    plt.scatter(x3, y3, s=sizes3, alpha=0.75, edgecolors="k", label=" AES-CBC", color='#e9ecb2')
    plt.scatter(x4, y4, s=sizes4, alpha=0.75, edgecolors="k", label=" AES-CTR", color='#f8b96b')
    plt.scatter(x5, y5, s=sizes5, alpha=0.75, edgecolors="k", label=" AES-GCM", color='red')
    plt.scatter(x6, y6, s=sizes6, alpha=0.75, edgecolors="k", label=" ASCON", color='#87cfd1')

    # Point labelling
    for x, y, label in zip(x1 + x2 + [x6[1], x6[3], x6[2]], y1 + y2 + [y6[1], y6[3], y6[2]], labels1 + labels2 + [labels6[1], labels6[3], labels6[2]]):
        plt.text(x + 2, y - 1, label, fontsize=7, ha='left', va='top', fontweight='bold')
    for x, y, label in zip(x3 + [x6[0]], y3 + [y6[0]], labels3 + [labels6[0]]):
        plt.text(x + 2.5, y + 1, label, fontsize=7, ha='left', va='center', fontweight='bold')
    for x, y, label in zip(x4 + x5, y4 + y5, labels4 + labels5):
        plt.text(x - 2, y, label, fontsize=7, ha='right', va='center', fontweight='bold')

    # Bubbles size legend
    legend_sizes = [size_factor * 128, size_factor * 192, size_factor * 256]
    for size in legend_sizes:
        plt.scatter([], [], s=size, alpha=0.6, edgecolors="k", facecolor='none', label=f" Taille de clé: {size // size_factor} bits")

    #Axes and graph legend
    plt.xlabel("Instructions/bit")
    plt.ylabel("Cycles/bit")
    plt.title("RISCV Benchmark")
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), scatterpoints=1, frameon=False, title="Légende", fontsize=9, labelspacing=2.5)
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    plt.tight_layout()

# Cycles per blocks number
if plot_cycles_per_blocks:
    plt.figure(figsize=(10, 6))

    # creating the trace for each algorithm
    for algo_name, data in algorithms.items():
        plt.errorbar(data['blocks'], data['mean_cycles'],
                     yerr=np.array([
                         [m - min_val for m, min_val in zip(data['mean_cycles'], data['min_cycles'])],
                         [max_val - m for m, max_val in zip(data['mean_cycles'], data['max_cycles'])]
                     ]),
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
        # Regresssion plotting
        #y_pred = [slope * xi + intercept for xi in data['blocks']]
        #plt.plot(data['blocks'], y_pred, '--', label=f'{algo_name} fit (R²={r_value**2:.2f})', color=data['color'])

    plt.xlabel('Nombre de blocs chiffrés')
    plt.ylabel('Nombre de cycles')
    plt.title('Nombre de cycles par algorithme en fonction du nombre de blocs')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), )

    if log_cycles_per_blocks:
        plt.xscale('log', base=2)
        plt.yscale('log', base=2)
    plt.tight_layout()
    print('')
    print('')

# Instructions per blocks number
if plot_instructions_per_blocks:
    plt.figure(figsize=(10, 6))

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

    if log_instructions_per_blocks:
        plt.xscale('log', base=2)
        plt.yscale('log', base=2)
    plt.tight_layout()


if plot_cycles_per_bit_per_blocks:
    plt.figure(figsize=(10, 6))

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
    plt.tight_layout()


if plot_instructions_per_bit_per_blocks :
    plt.figure(figsize=(10, 6))

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
    plt.tight_layout()

if plot_delta:
    plt.figure(figsize=(10, 6))

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
    plt.tight_layout()

# Cycles number per iteration number
if plot_cycles_per_iteration:
    # Subplots creation
    fig, axs = plt.subplot_mosaic([['1', '2'], ['3', '4']], layout='constrained', figsize=(10, 6))

    for i in ['1', '2', '3', '4']:
        ax = axs[i]
        for algo_name, data in algorithms.items():
            ax.errorbar(
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

    # Legend creation
    handles, labels = axs['4'].get_legend_handles_labels()
    fig.legend(handles, labels, loc='outside right upper', bbox_to_anchor=(1, 0.95))   # Position de la légende
    plt.tight_layout(rect=(0, 0, 0.75, 1))

# Cycles per AD size
if plot_cycles_per_ad:
    plt.figure(figsize=(10, 6))

    for algo_name, data in algorithms_AD.items():
        plt.errorbar(
            data['AD'], data['mean_cycles'],
            yerr=np.array([
                [m - min_val for m, min_val in zip(data['mean_cycles'], data['min_cycles'])],
                [max_val - m for m, max_val in zip(data['mean_cycles'], data['max_cycles'])]
            ]),
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

    plt.xlabel('AD (bits)')
    plt.ylabel('Cycles ')
    plt.title('Nombre de cycles par algorithme en fonction de la taille de l\'AD')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()

# Instructions per AD size
if plot_instructions_per_ad:
    plt.figure(figsize=(10, 6))

    for algo_name, data in algorithms_AD.items():
        plt.plot(data['AD'], data['instructions'],
                 label=algo_name,
                 color=data['color'],
                 marker=markers[data['style']],
                 markersize=4,
                 alpha=1,
                 linestyle='-',
                 linewidth=1)

    plt.xlabel('AD (bits)')
    plt.ylabel('Instructions ')
    plt.title('Nombre d\'instructions par algorithme en fonction de la taille de l\'AD')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()

plt.show()

