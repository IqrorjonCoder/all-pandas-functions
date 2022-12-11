import pandas as pd

df1 = pd.DataFrame({'a': [1,2,3,None],
                    'b': [4,5,6,None]})

df2 = pd.DataFrame({'a': [1,2,3,None],
                    'b': [4,5,6,None]}, index=['one', 'two', 'three', 'four'])

print(df1)
print(df1.reindex_like(df2))