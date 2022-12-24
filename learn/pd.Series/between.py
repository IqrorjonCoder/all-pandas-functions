import pandas as pd

d = [1,2,3,4]

data = pd.Series(d)

print(data)
print(data.between(left=2, right=3))