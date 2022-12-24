import pandas as pd

d = [1,2,3,0,None,-4]

data = pd.Series(d)

print(data)
print(data.all())