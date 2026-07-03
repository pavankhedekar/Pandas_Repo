import numpy as np

# Create a 1D array containing numbers from 1 to 24
arr = np.arange(1, 25)
print("array:", arr)
print("Shape:", arr.shape)

# Reshape into 4x6
arr_a = arr.reshape(4, 6)
print("\nReshaped to 4x6:\n", arr_a)
print("Shape:", arr_a.shape)

# Reshape into 3x8
arr_b = arr.reshape(3, 8)
print("\nReshaped to 3x8:\n", arr_b)
print("Shape:", arr_b.shape)

# Reshape into 2x3x4 (3D array)
arr_c = arr.reshape(2, 3, 4)
print("\nReshaped to 2x3x4 (3D array):\n", arr_c)
print("Shape:", arr_c.shape)
