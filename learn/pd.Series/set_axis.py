import pandas as pd

d = [1,2,3,None]

data = pd.Series(d).rename_axis('simplee')

print(data)
print(data.set_axis('simplee'))