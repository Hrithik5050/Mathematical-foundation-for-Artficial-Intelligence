import numpy as np
x = [12.1, 13.2, 15.6, 17.2, 18.8, 10.3, 11.7, 16.4]
y = [48, 59, 32, 18, 41, 32, 31, 30]
z = [101, 171, 112, 132, 140, 112, 151, 96]

#column stack the data to create a 2D array where each column represents a variable (x, y, z)
data = np.column_stack([x, y, z])
print(data)
#mean x y z
# Calculate means
#axis=0 means calculate mean for each column (x, y, z)
mean = np.mean(data, axis=0)
print("\nMean of x, y, z:")
print(mean)

#combine data and mean vstack is used for vertical stacking of arrays
data_with_mean = np.vstack([data,mean])
print("\nData with mean:")
print(data_with_mean)

#Covariance matrix
cov_matrix = np.cov( data, rowvar=0)

print("\nCovariance Matrix:")
print(cov_matrix)

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)