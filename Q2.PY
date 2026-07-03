import numpy as np

# Generate a 1D array of 20 random integers between 1 and 50
arr = np.random.randint(1, 51, size=20)

# Print the array
print("Array:", arr)

# Minimum value and its index (argmin)
print("Minimum value:", arr.min())
print("Index of minimum value (argmin):", arr.argmin())

# Maximum value and its index (argmax)
print("Maximum value:", arr.max())
print("Index of maximum value (argmax):", arr.argmax())

# Sum of all elements
print("Sum of elements:", arr.sum())

# Mean and Standard Deviation
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())
