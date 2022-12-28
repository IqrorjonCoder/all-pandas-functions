import pandas as pd

d = [1,2,None,-10]

data = pd.Series(d)

print(data)
for i, v in data.items():
    print(i, v)