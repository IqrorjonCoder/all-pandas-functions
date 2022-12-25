import pandas as pd

d = [1,2,3]

data = pd.Series(d, index=['one', 'two', 'three'])

print(data)
# print(data.groupby('one', axis=0))