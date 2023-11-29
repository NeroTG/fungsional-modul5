# import matplotlib.pyplot as plt
# import numpy as np

# # cara membuat sample data
# sample = np.random.normal(loc=50, scale=5, size=1000)

# # tampilkan dalam bentuk histogram:
# plt.figure(figsize=(5,4))
# plt.hist(sample, bins=10, density=True)
# plt.show()

# # np.random.normal(loc=50, scale=5, size=1000) digunakan untuk membuat 1000 sampel dari distribusi normal dengan rata-rata 50 dan standar deviasi 5. 
# # Kemudian, histogram dari sampel ini dibuat dengan plt.hist(sample, bins=10, density=True). 
# # Parameter density=True digunakan untuk menormalkan histogram sehingga total luas di bawah histogram adalah 1



# import numpy as np

# # cara membuat sample data
# sample = np.random.normal(loc=50, scale=5, size=1000)

# # menghitung mean dan standar deviasi
# sample_mean = np.mean(sample)
# sample_std = np.std(sample)

# print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))

# # np.mean(sample) digunakan untuk menghitung rata-rata sampel dan np.std(sample) digunakan untuk menghitung standar deviasi sampel.




# import numpy as np
# from scipy.stats import norm

# # cara membuat sample data
# sample = np.random.normal(loc=50, scale=5, size=1000)

# # menghitung mean dan standar deviasi
# sample_mean = np.mean(sample)
# sample_std = np.std(sample)

# # mendefinisikan distribusi normal
# dist = norm(sample_mean, sample_std)

# print(dist)

# # norm(sample_mean, sample_std) digunakan untuk mendefinisikan distribusi normal dengan rata-rata dan standar deviasi yang telah dihitung. 
# # Fungsi norm berasal dari pustaka scipy.stats.



# import numpy as np
# from scipy.stats import norm

# # cara membuat sample data
# sample = np.random.normal(loc=50, scale=5, size=1000)

# # menghitung mean dan standar deviasi
# sample_mean = np.mean(sample)
# sample_std = np.std(sample)

# # mendefinisikan distribusi normal
# dist = norm(sample_mean, sample_std)

# # membuat list nilai
# values = [value for value in range(30, 70)]

# # menghitung probabilitas untuk setiap nilai
# probabilitas = [dist.pdf(value) for value in values]

# print(probabilitas)

# # dist.pdf(value) digunakan untuk menghitung fungsi kepadatan probabilitas (pdf) dari distribusi normal untuk setiap nilai dalam values. 
# # Fungsi pdf mengembalikan probabilitas bahwa variabel acak yang mengikuti distribusi tertentu akan mengambil nilai tertentu.




import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# cara membuat sample data
sample = np.random.normal(loc=50, scale=5, size=1000)

# menghitung mean dan standar deviasi
sample_mean = np.mean(sample)
sample_std = np.std(sample)

# mendefinisikan distribusi normal
dist = norm(sample_mean, sample_std)

# membuat list nilai
values = [value for value in range(30, 70)]

# menghitung probabilitas untuk setiap nilai
probabilitas = [dist.pdf(value) for value in values]

# membuat histogram dari sample
plt.hist(sample, bins=10, density=True)

# menambahkan plot probabilitas distribusi
plt.plot(values, probabilitas)

plt.show()

# plt.hist(sample, bins=10, density=True) digunakan untuk membuat histogram dari sampel 
# plt.plot(values, probabilitas) digunakan untuk menambahkan plot probabilitas distribusi ke grafik yang sama.