import pandas as pd

d = [1,2,3,None]

data = pd.Series(d)

print(data)
print(data.compare(pd.Series([10,20,30,40]), result_names=('first', 'second')))