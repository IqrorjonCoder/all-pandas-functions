import pandas as pd

data = pd.MultiIndex.from_arrays([[1,2,3], [4,5,6]], names=['a', 'b'])

print(data)
print(data.get_level_values('a'))
print(data.get_level_values('b'))