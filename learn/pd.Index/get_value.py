import pandas as pd

data = pd.Index([1,2,3,None])

print(data)
print(data.get_value(pd.Series([0,1]), key=2))