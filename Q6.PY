import numpy as np

# Create a 5x5 matrix of random integers between 1 and 100
arr = np.random.randint(1, 101, size=(5, 5))
print("Original Matrix:\n", arr)

# 1. Print the diagonal elements
print("\nDiagonal elements:", np.diag(arr))

# 2. Print elements greater than 50
print("Elements greater than 50:", arr[arr > 50])

# 3. Replace all elements less than 30 with 0
arr[arr < 30] = 0

# 4. Print the modified array
print("\nModified Matrix:", arr)
