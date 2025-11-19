import numpy as np

# Day 3 — NumPy Basics

# 1. Creating arrays
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2. Array operations
print("Array * 2:", arr * 2)
print("Array + 5:", arr + 5)

# 3. 2D Array (Matrix)
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)

# 4. Matrix operations
print("Matrix Transpose:\n", matrix.T)
print("Matrix Sum:", matrix.sum())
print("Matrix Mean:", matrix.mean())

# 5. Random numbers (used in ML weight initialization)
random_nums = np.random.rand(5)
print("Random Numbers:", random_nums)
