import pandas as pd
from datetime import date, time

data = pd.Timestamp(year=2022, month=12, day=12, hour=12)

print(data)
print(data.combine(date=date(2005, 8, 24),
                   time=time(12,0,0)))