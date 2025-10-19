import pandas as pd

# INSERT

var = pd.DataFrame({"A" : [1,2,3,4,5] , "B" : [6,7,8,9,10]})
print(var)
print()
var.insert(1,"C",[11,12,13,14,15])
print(var)
print()

# DELETE USING POP FUNCTION

var.pop("B")
print(var)
print()

# DELETE USING DEL KEYWORD

del var["A"]
print(var)