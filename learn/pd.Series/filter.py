import pandas as pd

d = [None, 1, 2]

data = pd.Series(d, index=['one', 'two', 'three'])

print(data)
print(data.filter(regex=r'o'))