import numpy as np
nums1 = np.array([5, 15, 2])
nums2 = np.array([9, 15, 32])
np.set_printoptions(precision=15)
print("Original arrays:")
print(nums1)
print(nums2)
print("\nTest said two arrays are equal (element wise) or not:?")
print(nums1 == nums2)