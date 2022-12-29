import pandas as pd

d = [1,2,300]

data = pd.Series(d, index=['one', 'two', 'non'])

print(data)
print(data.reindex(['one', 'non', 'x']))