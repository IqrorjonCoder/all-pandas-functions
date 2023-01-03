import pandas as pd

data = pd.Index([1,1,2,2,3,3,None])

print(data)
print(data.drop_duplicates())