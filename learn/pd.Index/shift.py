import pandas as pd

data = pd.Index(pd.date_range('1/1/2005', periods=5, freq='1D'))

print(data)
print(data.shift(2))