import pandas as pd

d = [1,2,3,None]

data = pd.Series(d)

print(data)
print(data.sort_values(ascending=False, na_position="first"))