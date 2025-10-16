import numpy as np

var = np.array([1,2,3,4,5])
print(var)
co = var.copy()
var[1] = 40
print(co)
vi = var.view()
vi[2] = 50
print(vi)
print(var)

#copy:
#The copy owns the data.The copy of an array is a new array..The changes made in the copy data does not reflect in the original array...

#view
#The view does not own the data,A view of the orriginal array.Any changes made to the view willl affect the original array and vice versa