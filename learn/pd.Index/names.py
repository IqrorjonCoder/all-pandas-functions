import pandas as pd

data = pd.MultiIndex.from_arrays([[1,2],[None,-100]], names=['one', 'two'])

print(data)
print(data.names)