import pandas as pd

data = pd.Index([1,2,100])

print(data)
print(data.equals(pd.Index([1,2,100])))
print(data.equals(pd.Index([1,2,200])))