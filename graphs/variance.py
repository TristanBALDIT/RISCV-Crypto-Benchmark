import matplotlib.pyplot as plt
from data import algorithms_var

for algo_name, data in algorithms_var.items():
    data['delta'] = []
    data['mean'] = []
    data['var'] = []
    for data_name, d in data.items():
        if 'data' in data_name and len(d) != 0:
            sum = 0
            delta = max(d) - min(d)
            data['delta'].append(delta)

            for i in d:
                sum += i

            m = sum / len(d)
            data['mean'].append(m)
            var = 0

            for i in d:
                var += (i - m) ** 2
            var = var / len(d)
            data['var'].append(var)

            print(algo_name, data_name, m, var, delta)
    print('')

print(algorithms_var['ChaCha20']['var'])

plt.figure(figsize=(10, 6))
plt.plot(algorithms_var['ChaCha20']['data-1000'])
plt.xlabel('Nombre de blocs chiffrés')
plt.ylabel('Cycles / Bit')

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

display_algo = ['ChaCha20', 'AES-CTR-128', 'AES-GCM-128', 'AES-GCM-192']
counter = 0

for ax in axes.flat:
    ax.plot(algorithms_var[display_algo[counter]]['data-1000'])
    ax.set_title(display_algo[counter])
    counter += 1

fig.suptitle('Evolution du nombre de cycles en fonction des itérations', fontsize=16)

markers = ['o', 's', 'D', '^', 'v', '<', '>']

plt.figure(figsize=(10, 6))
for algo_name, data in algorithms_var.items():
    plt.plot([50, 100, 500, 1000], data['var'],
             label=algo_name,
             color=data['color'],
             marker=markers[data['style']],
             markersize=4,
             alpha=1,
             linestyle='-',
             linewidth=1)

plt.xlabel('Numéro d\'itération')
plt.ylabel('Variance du nombre de cycles')
plt.title('Variance du nombre de cycles par algorithme en fonction des itérations')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()

plt.show()
