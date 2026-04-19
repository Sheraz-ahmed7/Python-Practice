#Perform mathematical operations on multi-dimensional data.
import numpy as np
#Create a NumPy array of shape (3, 5) filled with the value 7.
array = np.full((3, 5), 7)
# print(array)
#Change all values in the third column to 0.
array[:, 2] = 0
# print(array)
#Add 10 to every element in the first row.
array[0] += 10
# print(array)
#Flatten the (3, 5) array into a 1D array of 15 elements.
flattened_array = array.flatten()
print(flattened_array)
