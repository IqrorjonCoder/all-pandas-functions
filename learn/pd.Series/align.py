import pandas as pd

d = [1,2,3,None]

data = pd.Series(d)

print(data, "\n\n")
print(data.align(pd.Series([10,20,30,40])))