import datetime

import pandas as pd

data = pd.Timestamp(year=2022, month=12, day=12)

ttt = datetime.datetime.timestamp(datetime.datetime.now())
print(data, f"\ntimestamp: {ttt}")
print(data.fromtimestamp(ttt))