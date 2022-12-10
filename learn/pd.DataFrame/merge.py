import pandas as pd

df1 = pd.DataFrame({'a': [1,2,3],
                    'b': [4,5,6]})
df2 = pd.DataFrame({'c': [1,2,3],
                    'd': [0,-1,-2]})

print(df1, df2)
df1 = df1.merge(df2, left_on='a', right_on='c')

print(df1)