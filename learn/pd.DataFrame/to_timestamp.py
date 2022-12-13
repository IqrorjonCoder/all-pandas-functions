import pandas as pd

df1 = pd.DataFrame({
    'a': pd.date_range('1/1/2005', periods=3, freq='1D'),
}).set_index(pd.RangeIndex(start=0, step=1, stop=3))


print(df1)
print(df1.to_timestamp())