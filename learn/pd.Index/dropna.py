import pandas as pd

data = pd.Index([1,2,3,100,None,None])

print(data)
print(data.dropna(how="any"))