import pandas as pd

data = pd.Index([4,2,3])

print(data)
print(data.to_series(index=['one', 'two', 'three']))