import pandas as pd

data = pd.MultiIndex.from_arrays([[1,2],[3,None]], names=['a', 'b'])

print(data)
print(data.droplevel('a'))