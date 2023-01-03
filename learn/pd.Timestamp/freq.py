import pandas as pd

data = pd.Timestamp(year=2022, month=12, day=12, hour=12, freq='10D')

print(data)
print(data.freq)