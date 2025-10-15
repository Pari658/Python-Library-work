import numpy as np

#using shape
arr = np.array([[1,2,3],[1,2,4]])
print(arr)
print()
print(arr.shape)
print()

arr2 = np.array([[[1,2,3],[1,2,4]]])
print(arr2)
print()
print(arr2.shape)

#using reshape

initial = np.array([5,6,7,8,9,2])
res = initial.reshape(3,2)
print(res)
print(res.ndim)
back = res.reshape(-1)#reshape back to original one dimension 
print(back)