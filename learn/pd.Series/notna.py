import pandas as pd

d = [-10,None,1]

data = pd.Series(d)

print(data)
print(data.notna())