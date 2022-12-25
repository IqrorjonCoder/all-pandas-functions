import pandas as pd

d = [1.100, 2, None, -10, True]

data = pd.Series(d)

print(data)
print(data.convert_dtypes())