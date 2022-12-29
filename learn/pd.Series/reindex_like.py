import pandas as pd

d = [1,2,300]

data = pd.Series(d, index=['one', 'two', 'non'])

print(data)
print(data.reindex_like(pd.Series([100,200,3], index=['one', 'two', 'n'])))