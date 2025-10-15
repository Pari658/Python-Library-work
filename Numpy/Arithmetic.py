import numpy as np
#for 1D ARRAY

#Addition
arr = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
# varAdd = arr + arr2
varAdd = np.add(arr,arr2)
print(varAdd)
print()


#substraction
arr = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
# varAdd = arr - arr2
varAdd = np.subtract(arr,arr2)
print(varAdd)
print()

#multiplication

arr = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
# varAdd = arr * arr2
varAdd = np.multiply(arr,arr2)
print(varAdd)
print()

#divide

arr = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
# varAdd = arr / arr2
varAdd = np.divide(arr,arr2)
print(varAdd)
print()

#modulas

arr = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
# varAdd = arr % arr2
varAdd = np.mod(arr,arr2)
print(varAdd)
print()


#power

arr = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
# varAdd = arr ** arr2
varAdd = np.power(arr,arr2)
print(varAdd)
print()

#reciprocal
arr = np.array([1,2,3,4])
varAdd = np.reciprocal(arr)
print(varAdd)
print()

#FOR 2D ARRAY

var1 = np.array([[1,2,3],[1,2,3]])
var2 = np.array([[1,2,3],[1,2,3]])
final = np.add(var1,2)
print(final)
print()
#Basic arithmatic function

# min and max

basic = np.array([1,2,3])
print(np.min(basic),np.max(basic))
print()

#argmin and argmax [for index of min and max]

print(np.argmax(basic),np.argmin(basic))
print()

#sqrt

print(np.sqrt(basic))
print()

#sin and cos value

print(np.sin(basic))
print(np.cos(basic))
print()

#cumsum [cumulative sum]

print(np.cumsum(basic))