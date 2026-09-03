import numpy as np

x = [12.1, 13.2, 15.6, 17.2, 18.8, 10.3, 11.7, 16.4]
y = [48, 59, 32, 18, 41, 32, 31, 30]
z = [101, 171, 112, 132, 140, 112, 151, 96]

data = np.array([x, y, z])

cov_matrix = np.cov(data)

print(cov_matrix)