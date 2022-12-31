import pandas as pd

d = [1,2,3]

data = pd.Series(d)

print(data)
data.update([100,200,300])
print(data)