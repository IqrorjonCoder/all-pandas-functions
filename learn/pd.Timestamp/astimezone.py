import pandas as pd

data = pd.Timestamp(year=2022,month=12,day=12,hour=12, tz='Asia/Dacca')

print(data)
print(data.astimezone(tz='Asia/Tashkent'))