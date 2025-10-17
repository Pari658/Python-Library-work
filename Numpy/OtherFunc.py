import numpy as np

# SEARCHING
# 1D ARRAY
var = np.array([1,2,3,4,5,6])
x = np.where((var % 2) == 0)
print(x)
place = np.searchsorted(var,2.5)
print(place)
print()
#2D ARRAY
var2 = np.array([[1,2],[3,4]])
y = np.where(var2 == 4)
print(y)
print()

# SORTING
# 1D ARRAY
s = np.array([2,3,5,1,4])
a = np.array(['a','c','b'])
print(np.sort(s))
print(np.sort(a))
#2D ARRAY
s2 = np.array([[5,3],[9,4]])#sorting happens row wise...
print(np.sort(s2))
print()

# FILTER
# 1D ARRAY
a = np.array(['a','c','b', 'f','e'])
fil = [True,False,True,False,True]
new_a = a[fil]
print(new_a)
print()

# SHUFFLE
suf = np.array([1,2,3,4,5,6])
np.random.shuffle(suf)
print(suf)

# UNIQUE
uni = np.array([1,2,3,4,1,2,3,4,5,6,])
uni_new = np.unique(uni)
print(uni_new)

# RESIZE
res = np.resize(uni_new,(2,5))
print(res)

# FLATTEN
f = res.flatten()
print(f)

# RAVEL
r = np.ravel(res)
print(r)

# INSERT 
ins = np.array([1,2,3,4])
v = np.insert(ins,2,6)
print(v)

# DELETE
d = np.delete(ins,2)
print(d)