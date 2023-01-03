import pandas as pd

data = pd.Index([1,2,None,100-100])

print(data)
print(data.fillna(value="na_X"))