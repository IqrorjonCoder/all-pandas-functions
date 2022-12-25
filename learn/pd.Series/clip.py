import pandas as pd

d = [1,2,3,4,5,6]

data = pd.Series(d)

print(data)
print(data.clip(2, 5))