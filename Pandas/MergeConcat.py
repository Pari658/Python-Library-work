import pandas as pd

dt1 = pd.DataFrame({"A" : [1,2,3,4,5],"B" : [6,7,8,9,10]})
dt2 = pd.DataFrame({"B" : [6,7,8,9,10],"C" : [6,66,8,77,10]})
# on = "common column to merge"
# how = "left/right/outer/inner"
# indicator=True [ both merge or not ]
print(pd.merge(dt1,dt2, on = "B",))
print()

# concatenation

s1 = pd.Series([1,2,3,4])
s2 = pd.Series([5,6,7,8])
print(pd.concat([s1,s2]))
print()
print(pd.concat([dt1,dt2],axis=1,join="inner"))
