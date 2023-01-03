import pandas as pd

data = pd.Index([4,2,3,None,-100])

print(data)
print(data.to_numpy())