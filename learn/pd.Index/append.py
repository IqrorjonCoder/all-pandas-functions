import pandas as pd

data = pd.Index([1,2,3])

print(data)
print(data.append(pd.Index([100,200])))