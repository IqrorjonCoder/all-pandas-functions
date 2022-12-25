import pandas as pd

d = [1,2,3]

data = pd.Series(d)

print(data)
print(data.gt(pd.Series([10,1,3])))