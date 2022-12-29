import pandas as pd
import random
import datetime

d = pd.date_range('1/1/2005', periods=10, freq='1D')

data = pd.Series(random.random(), index=d)

print(data)
print(data.rolling(window=datetime.timedelta(days=3)))