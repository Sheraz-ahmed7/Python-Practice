import numpy as np

a = np.array([1,2,3])
print(a)

print("2D array: ")
b = np.array([[2.3,3,5,7],[9.0,8.7,6,7]])
print(b)

#get dimension:
print(a.ndim)

#get shape:
print(b.shape)

#get type:
print("arrray type: ",b.dtype)

#get size:
print("arrray size: ",b.itemsize)
#get total size:
print("arrray size: ",b.nbytes)

