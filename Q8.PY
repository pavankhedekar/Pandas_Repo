import numpy as np

# Create two 3x3 matrices
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

b = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])

print("Matrix A:\n", a)
print("\nMatrix B:\n", b)

# 1. Element-wise multiplication
elementwise = a * b
print("\nElement-wise multiplication:\n", elementwise)

# 2. Matrix multiplication
matrix_mult = a @ b
print("\nMatrix multiplication:\n", matrix_mult)
