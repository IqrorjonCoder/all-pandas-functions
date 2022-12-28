import pandas as pd

d = [-10,None,1,20,30]

data = pd.Series(d)

print(data)
print(data.nsmallest(2))