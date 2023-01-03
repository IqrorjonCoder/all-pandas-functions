import pandas as pd

data = pd.Index([1,2,True])

print(data)
print(data.is_boolean())
print(pd.Index([True, False]).is_boolean())