import numpy as np

# Generate a 66 matrix of random numbers using np.random.randn().
arr = np.random.randn(6, 6)
print("Original Matrix:\n", arr)

# Print shape, size, and dtype
print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# Find the index of maximum and minimum value
print("\nIndex of maximum value:", arr.argmax())
print("Index of minimum value:", arr.argmin())

# Extract the top-left 3x3 submatrix
submatrix = arr[:3, :3]
print("\nTop-left 3x3 submatrix:\n", submatrix)

# Replace all negative numbers with their absolute value
arr[arr < 0] = np.abs(arr[arr < 0])
print("\nModified Matrix:\n", arr)

# Print the mean of the modified matrix
print("\nMean of modified matrix:", arr.mean())
