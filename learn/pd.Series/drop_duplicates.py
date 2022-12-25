import pandas as pd

d = [1,1,2,2,3,4,4]

data = pd.Series(d)

print(data)
print(data.drop_duplicates())