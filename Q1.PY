import numpy as np

# Create a 2D array of shape (5, 6) with random integers between 10 and 100
arr = np.random.randint(10, 101, size=(5, 6))

# Print the array
print("Array:", arr)

# Print properties
print("Shape of the array:", arr.shape)
print("Total number of elements (size):", arr.size)
print("Data type (dtype):", arr.dtype)
