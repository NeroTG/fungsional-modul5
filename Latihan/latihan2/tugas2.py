import matplotlib.pylab as plt
import numpy as np

# xpoints = np.array([1, 8, 10])
# ypoints = np.array([3, 10, 5])

# plt.figure(figsize=(5,5))
# plt.plot(xpoints, ypoints, color='red')
# plt.xlim([0,15])
# plt.ylim([0,15])
# plt.show()



# telah di modifikasi

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(7,7))
plt.plot(xpoints, ypoints, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=12)
plt.xlim([0,15])
plt.ylim([0,15])

# Menambahkan judul dan label
plt.title('Grafik Percobaan 2')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Menambahkan grid
plt.grid(True)

# Menambahkan teks
for (i, j) in zip(xpoints, ypoints):
    plt.text(i, j, f'({i},{j})')

plt.show()

