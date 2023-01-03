import pandas as pd

data = pd.Index([1,2,-100,'None'])

print(data)
print(data.is_numeric())
print(pd.Index([1,2,3]).is_numeric())