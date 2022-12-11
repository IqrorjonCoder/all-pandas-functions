import pandas as pd

df1 = pd.DataFrame({'a': [1,2,3,None],
                    'b': [4,5,6,None]})

print(df1)
print(df1.rank(na_option="bottom"))