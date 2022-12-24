import pandas as pd

d = [1,2,3,-100]

data = pd.Series(d)

print(data)
print(data.at[0])