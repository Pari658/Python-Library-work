#consider 1D Array [1 2 3]  indexing will start from 0,1,2,3 so on.. there is also negative indexes the last element will be -1 so it goes like.. -4,-3,-2,-1 #for multi dimension simple logic of c language array concept.

#[2,3,4,5]
#[0,1,2,3] positive index
#[-4,-3,-2,-1] negative index

import numpy as np

var = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(var[0][-1][-2])
print(var)

#Slicing in array

var2 = np.array([1,2,3,4,5])
print(var2[0:3:1])#[start_index : stop_index + 1 : step]
print(var2[1:]) #from index to everything
print(var2[:4])#upto index 3

print()

#slicing NDarray
print(var[0][1][0:])