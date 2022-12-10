import pandas as pd

df1 = pd.DataFrame({'a': [1,2,3,None],
                    'b': [4,5,6,None]})

print(df1)
print(df1.rename(columns={'a': 'A', 'b': 'B'}))
print(df1.rename(index={0:'zero', 1:'one', 2:'two', 3:'three'}))