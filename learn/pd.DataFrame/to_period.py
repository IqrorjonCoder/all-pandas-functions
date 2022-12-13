import pandas as pd

df1 = pd.DataFrame({
    'a': [True, None, False],
    'b': [6,7,8],
    'c': [60.12,7.32,8.65],
}).set_index(pd.date_range('1/1/2005', freq='1D', periods=3))

print(df1)
print(df1.to_period('M'))
print(df1.to_period('Y'))