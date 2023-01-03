import pandas as pd

data = pd.Index([1,2,3,None])

print(data)
print(data.isin([100,200,1]))