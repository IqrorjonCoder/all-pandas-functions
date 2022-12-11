import pandas as pd

df1 = pd.DataFrame({'a': ['1',1,3,10],
                    'b': [4,5,6,10],
                    'c': [-10,-20,-30,-40]})

print(df1)
print(df1.replace(1, 1000))
print(df1.replace(r'1$', 'salomchaa', regex=True))