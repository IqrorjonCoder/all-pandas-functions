import pandas as pd

d = [1,2,None]

data = pd.Series(d, index=['one', 'two', 'three'])

print(data)
print(data.keys())