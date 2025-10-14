import numpy as np

#rand() [numbers are between 0 and 1]

var = np.random.rand(4)
print(var)
print()

var2 = np.random.rand(3,3)
print(var2)
print()

#randn() [pos and neg numbers but close to 0]

fun = np.random.randn(3)
print(fun)
print()
fun2 = np.random.randn(2,2)
print(fun2)
print()

#ranf() [numbers between 0 and 1 but does not include 1] and excepts at most 1 argument only

funRanf = np.random.ranf(4)
print(funRanf)
print()

#randint() [number are from particular range]

funRandint = np.random.randint(1,100,5)
print(funRandint)
print()
