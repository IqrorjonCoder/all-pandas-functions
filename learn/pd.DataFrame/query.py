import pandas as pd

df1 = pd.DataFrame({'a': [1,2,3,10],
                    'b': [4,5,6,10]})

print(df1)
print(df1.query('a > b'))