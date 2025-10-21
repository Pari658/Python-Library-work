import pandas as pd

var = pd.read_csv("prac2.csv")
print(var)
print()

# dropna()
print(var.dropna())

# Parameters

# axis = 0 [drop row with Nan]
# axis = 1 [drop columns with Nan]
# how = "any" [drop row with any cell containing Nan]
# how = "all" [drop row contaning all Nan]
# subset = ["column_name"] [drop column with any cell contaning Nan]
# inplace = True [change original dataframe]
# inplace = False [returns new dataframe]
# thresh = 2 [Minimum number of non-NaN values required to keep a row/column.]

#fillna 

print(var.fillna('pari'))

# paramters
# method ['ffill' → forward fill,'bfill' → backward fill]
# limit 


