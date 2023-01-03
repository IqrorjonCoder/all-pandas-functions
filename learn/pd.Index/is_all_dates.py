import pandas as pd

data = pd.Index(pd.date_range('1/1/2005', periods=3, freq='1H'))

print(data)
print(data.is_all_dates)
print(pd.Index([1,2,3]).is_all_dates)