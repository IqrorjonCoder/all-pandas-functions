import pandas as pd

df1 = pd.DataFrame({
    'a': [True, None, False],
    'b': [6,7,8],
    'c': [60.12,7.32,8.65],
}).set_index(pd.date_range('1/1/2005', periods=3, freq='1H', tz='Europe/Berlin'))


print(df1)
print(df1.tz_convert(tz='US/Central'))
