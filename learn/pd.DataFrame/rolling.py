import pandas as pd

df1 = pd.DataFrame({'a': [1,2,3,4,5]}).set_index(pd.date_range('/1/1/2005', periods=5, freq='1D'))

print(df1)
print(df1.rolling(3).sum())