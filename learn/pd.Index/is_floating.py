import pandas as pd

data = pd.Index([1,2,-100,None])

print(data)
print(data.is_floating())