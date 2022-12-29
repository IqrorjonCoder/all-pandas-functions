import pandas as pd

d = [1,2,None]

data = pd.Series(d)

print(data)
print(data.ravel())
print(data.ravel().tolist())