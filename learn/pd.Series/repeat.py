import pandas as pd

d = [1,2,3,None]

data = pd.Series(d)

print(data)
print(data.repeat(2))
print(data.repeat([1,2,1,1]))