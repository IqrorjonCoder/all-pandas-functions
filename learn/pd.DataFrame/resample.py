import pandas as pd

df1 = pd.DataFrame({'a': [i for i in range(10)]}).set_index(pd.date_range('1/1/2005', periods=10, freq='1D'))

print(df1)
print(df1.resample('2D').sum())