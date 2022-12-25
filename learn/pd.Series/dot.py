import pandas as pd

d = [1,2]

data = pd.Series(d)

print(data)
print(data.dot(pd.Series([10,20])))
print(data @ (pd.Series([10,20])))