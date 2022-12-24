import random
import pandas as pd

d = pd.date_range('1/1/2022', periods=10, freq='1H')

data = pd.Series(random.random(), index=d)

print(data)
print(data.between_time('4:00', '9:00'))