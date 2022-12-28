import pandas as pd

d = [1,2,3,-40]

data = pd.Series(d)

print(data)
print(data.loc[[0, 1]])