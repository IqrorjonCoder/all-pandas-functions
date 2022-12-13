import pandas as pd

df1 = pd.Series(range(7),
              index=pd.DatetimeIndex(['2018-10-28 01:30:00',
                                      '2018-10-28 02:00:00',
                                      '2018-10-28 02:30:00',
                                      '2018-10-28 02:00:00',
                                      '2018-10-28 02:30:00',
                                      '2018-10-28 03:00:00',
                                      '2018-10-28 03:30:00']))


print(df1)
print(df1.tz_localize('CET'))
