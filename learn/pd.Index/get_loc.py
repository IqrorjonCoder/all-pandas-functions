import pandas as pd

data = pd.Index(['a', 'b', 'c'])

print(data)
print(data.get_loc('a'))
print(data.get_loc('b'))