import pandas as pd

data = pd.Index([1,2,100,-100,-100])

print(data)
print(data.duplicated())