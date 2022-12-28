import pandas as pd

d = [-10,None,1,None,1,2,20,3,2]

data = pd.Series(d)

print(data)
print(data.nunique(dropna=False))