import numpy as np
mat = np.matrix([[1,2,3],[4,5,6],[7,8,6]])
mat2 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(mat)
print(mat2)

# Addition
print(mat + mat2)

# Substraction
print(mat - mat2)

# Multiplication
print(mat * mat2)
print(mat.dot(mat2))
print() 

# Transpose
print(np.transpose(mat))
print()

# Swapaxes
print(np.swapaxes(mat,1,0))
print()

# Inverse
print(np.invert(mat))
print()

# Power 
print(np.power(mat,10))
print()

# Determinate
print(np.linalg.det(mat))
print()
