import pandas as pd

data = pd.Index([1,2,3])

print(data)
print(data.putmask(mask=[True, True,False], value=[100, 200, 300]))