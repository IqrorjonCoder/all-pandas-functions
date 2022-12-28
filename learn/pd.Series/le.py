import pandas as pd

d = [1,2,3,11,None]

data = pd.Series(d)

print(data)
print(data.le(10))