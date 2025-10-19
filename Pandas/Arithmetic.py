import pandas as pd

var = pd.DataFrame({"A" :[1,2,3,4], "B" : [5,6,7,8]})
print(var)

# addition
print()
var["C"] = var["A"] + var["B"]
print(var)

# subtraction
print()
var["C"] = var["A"] - var["B"]
print(var)

# multiplication
print()
var["C"] = var["A"] * var["B"]
print(var)


# division
print()
var["C"] = var["A"] / var["B"]
print(var)


# power
print()
var["C"] = var["A"] ** var["B"]
print(var)


# modulo
print()
var["C"] = var["A"] % var["B"]
print(var)
print()

# conditions

var["A <= 3"] = var["A"] <= 3
var["B > 5"] = var["A"] > 5
print(var)