import pandas as pd

# using list
list = [1,2,3,4,5,6]
var = pd.DataFrame(list)
print(var)
print(type(var))

# using dictionary

dict = {
  "a" : [1,2,3,4,5],
  "b" : [6,7,8,9,10],
}
var2 = pd.DataFrame(dict)
print(var2["a"][2])

#using multiple list

list_1 = [[1,2,3,4,5],[11,12,13,14,15]]
print(pd.DataFrame(list_1))