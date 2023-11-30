import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [3, 7, 2, 8, 5]

# plt.scatter(x, y)
# plt.show()


# telah di modifikasi

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Membuat scatter plot dengan variasi warna dan ukuran titik
plt.scatter(x, y, color='red', s=100, edgecolors='black')

# Menambahkan judul dan label sumbu
plt.title('Scatter Plot Percobaan 4')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menampilkan grid
plt.grid(True)
plt.show()
