import pandas as pd

data = pd.Index([1,2,3,None])

print(data)
print(data.join(pd.Index([100,200]), how='right'))