import pandas as pd
import random

d = pd.date_range('1/1/2005', periods=10, freq='1H', tz='Asia/Tashkent')

data = pd.Series(random.random(), index=d)

print(data)
print(data.tz_convert(tz='America/Los_Angeles'))