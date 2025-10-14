import numpy as np

#Fill all the elements with zeroes

arrZero = np.zeros(4)
arrZero1 = np.zeros((3,4))

print(arrZero)
print()
print(arrZero1)
print()

# #Fill elements with all one

arrOne = np.ones(4)
arrOne1 = np.ones((3,4))

print(arrOne)
print()
print(arrOne1)
print()

# empty elements

arrEmpty = np.empty(4)
print(arrEmpty)
print()

# creating array using range function

arrRange = np.arange(4)
print(arrRange)
print()

#Array Diagonal element filled with 1s

arrDiagonal = np.eye(3,3)
print(arrDiagonal)
print()

#create an Array with values that are spaced linearly in a specified interval
arrLins = np.linspace(0,20,num = 5)
print(arrLins)
