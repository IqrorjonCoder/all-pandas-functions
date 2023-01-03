import pandas as pd

data = pd.Index(list('aaabbccd'))

print(data)
print(data.get_slice_bound('a', side='right'))
print(data.get_slice_bound('b', side='left'))
print(data.get_slice_bound('b', side='right'))