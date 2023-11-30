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
