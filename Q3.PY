import numpy as np

# Create a 4x5 matrix of random integers between 20 and 80
arr = np.random.randint(20, 81, size=(4, 5))

# Print the matrix
print("Matrix:\n", arr)

# Minimum and maximum value
print("Minimum value:", arr.min())
print("Maximum value:", arr.max())

# Sum of all elements
print("Sum of all elements:", arr.sum())

# Mean and Standard Deviation
print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())

# Sum of each row
print("row sum : ")
for row in arr:
    print(sum(row)) 

# Sum of each column
print("column sum : ")
for column in arr:
    print(sum(column))
