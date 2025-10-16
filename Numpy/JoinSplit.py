import numpy as np

#JOIN

var1 = np.array([1,2,3])
var2 = np.array([4,5,6])

#To join two 1D arrays
ar = np.concatenate((var1,var2))
print(ar)
#To join two 2D arrays

var1 = np.array([[1,2],[2,3]])
var2 = np.array([[1,2],[2,3]])
ar_new = np.concatenate((var1,var2),axis=1)
print(ar_new)

#using stack function

var_1 = np.array([[1,2],[2,3]])
var_2 = np.array([[4,5],[5,6]])
new = np.stack((var_1,var_2),axis=1)
print(new)
print()
print(np.hstack((var_1,var_2)))#row
print()
print(np.vstack((var_1,var_2)))#column
print()
print(np.dstack((var_1,var_2)))#height
print()

#SPLIT

#spliting 1D array
arr1 = np.array([1,2,3,4,5,6])
arr1_new = np.array_split(arr1,3)
print(arr1_new[1])
print()

#spliting 2D array
arr2 = np.array([[1,2],[3,4],[4,5]])
arr2_new = np.array_split(arr2,3)
print(arr2_new)