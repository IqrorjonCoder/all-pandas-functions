import pandas as pd

data = pd.Index([1,1,2])

print(data)
print(data.identical(pd.Index([1,1,2])))
print(data.identical([1,1,2]))