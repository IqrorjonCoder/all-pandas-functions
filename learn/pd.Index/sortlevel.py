import pandas as pd

data = pd.MultiIndex.from_arrays([[10,2,3], [4,5,6]], names=['a', 'b'])

print(data)
print(data.sortlevel('a'))
print(data.sortlevel('b', ascending=False))