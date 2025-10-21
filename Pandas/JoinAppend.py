import pandas as pd

var1 = pd.DataFrame({"C" : [1,20,30,4], "D" : [20,3,40,5]})
var2 = pd.DataFrame({"A" : [1,2,3,4], "B" : [2,3,4,5]})

print(var1.join(var2))
print()

# group by
var3 = pd.DataFrame({"name" : ["a","b", "c","d","a","a","c","d"], "Sub" : [12,13,14,12,15,14,13,12]})
print(var3)
print()

var_new =  var3.groupby("name")
print(var_new)

for x,y in var_new:
  print(x)
  print(y)