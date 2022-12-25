import pandas as pd

d = [1,2,3,4]

data = pd.Series(d)

print(data)
print(data.combine(pd.Series([10,20,-30,-40]), max))