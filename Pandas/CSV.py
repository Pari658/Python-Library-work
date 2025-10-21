# Write CSV file
import pandas as pd

dict = {
  "A" : [1,2,3,4,5],
  "B" : [6,7,8,9,10],
  "C" : [11,12,13,14,15],
}
var = pd.DataFrame(dict)
var.to_csv("Learning.csv", index = False,header=["C1","C2","C3"])
print(var)

# Read CSV file 

# --- PARAMETERS ---
# nrows=4,
# usecols = ["C2"]
# skiprows = [0]
# index_col="C1"
# header=2
# names=["P"]
# dtype={"C3" : "float"}

csv_read = pd.read_csv("Learning.csv", ) 
print(csv_read)

# Pandas Functions for CSV

csv_1 = pd.read_csv("Practise.csv")

# getting just index number
print(csv_1.index)

# getting column names
print(csv_1.columns)
print()

# getting max,min,count,std...
print(csv_1.describe)
print()

# head() and tail()
print(csv_1.head(3))
print(csv_1.tail(3))

# turning into array
print(csv_1.to_numpy)

# sorting
print(csv_1.sort_index(axis = 0,ascending=False))

#changing data
# does not changes in original file.
# csv_1["Name"][0] = "Pari Patel"
# print(csv_1)

csv_1.loc[0,"Name"] = "Pari Patel"
print(csv_1)

print(csv_1.loc[[4,5] , ["Name","Department"]])
print(csv_1.iloc[0,2])

