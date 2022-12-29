import pandas as pd

d = [1,2,300]

data = pd.Series(d)

print(data)
print(data.rename_axis('simpee'))