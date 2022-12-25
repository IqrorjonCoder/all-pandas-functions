import pandas as pd

d = [1,2,3]

data = pd.Series(d)

print(data)
print(data.ge(pd.Series([10,2,3])))