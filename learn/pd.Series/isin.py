import pandas as pd

d = [1,2,3,4]

data = pd.Series(d)

print(data)
print(data.isin([5]))
print(data.isin([3,2]))