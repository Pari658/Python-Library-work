import numpy as np
# y = np.array([1,2,3,4])
# print(type(y))

# demoList = []
# for i in range(1,5):
#   x = int(input(f"Enter the value {i} : "))
#   demoList.append(x)

# arr = np.array(demoList)
# print(np.ndim(arr))
# print(arr.ndim)

arr2 = np.array([[1,2] , [2,3] ,[3,4]])
print(arr2)
print(np.ndim(arr2))

arr3 = np.array([[[1,2,3] , [3,4,5] , [6,7,8]]])
print(arr3)
print(np.ndim(arr3))

arrn = np.array([1,2],ndmin=10)
print(arrn)
print(np.ndim(arrn))