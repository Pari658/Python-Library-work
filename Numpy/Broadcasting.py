import numpy as np

var1 = np.array([1,2,3])
print(var1.shape)
print()
print(var1)
print()

var2 = np.array([[1],[2],[3]])
print(var2.shape)
print()
print(var2)
print()

#broadcasting happens bacause atleast one or n was 1 (m x n) in both array or same dimensions occurs..and resulting array will me a x b  where a is max(m1,m2)and b is max(n1,n2)

print(var1 + var2) 