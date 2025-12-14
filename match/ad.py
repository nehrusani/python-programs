import numpy as np

nums = input("Enter numbers separated by space: ")
a = np.array(nums.split(), dtype=int)
print(a)
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))