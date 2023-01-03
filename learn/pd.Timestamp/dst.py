import pandas as pd

data = pd.Timestamp(year=2022, month=12, day=12, hour=12, minute=30, second=10)

print(data)
print(data.dst())