import pandas as pd
a = pd.Series([1,2,3],dtype = "float")
print(a)
print(type(a))
print(a[1])

a_index = pd.Series([1,2,3,4,5] , index=['a','b','c','d','e'])
print(a_index)

dict = {
  "name" : "pari",
  "age" : 18
}
dict2 = {
  "name" : ['python','c','c++','java']
}

a_dict = pd.Series(dict)
print(a_dict)
a_dict2 = pd.Series(dict2)
print(a_dict2)

num = pd.Series(12,index=[1,2,3,4])
num2 = pd.Series(12,index=[1,2,3,4,5,6,7])
print(num + num2)
