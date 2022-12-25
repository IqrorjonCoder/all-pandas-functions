import pandas as pd

d = [1,1,None,2,3,None,4]

data = pd.Series(d)

print(data)
print(data.dtypes)