import pandas as pd

d = [1,2,3,4,4,1,None]

data = pd.Series(d)

print(data)
print(data.unique())