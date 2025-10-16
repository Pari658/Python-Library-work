import numpy as np

var = np.array([1,2,3,4,5,6,7])
var1 = np.array([[1,2,3],[4,5,6]])

#using "for" loop for 1D array
for i in var:
  print(i)

print()

#using "for" loop for 2D array
for i in var1:
  for j in i:
    print(j)
print()

#using nditer function flags=['buffered'],op_dtypes=["S"] for changing data type
for i in np.nditer(var1):
  print(i)
print()

#ndenumerate for finding indexes also..
for i in np.ndenumerate(var1):
  print(i)
print()

