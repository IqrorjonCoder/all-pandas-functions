import pandas as pd

df1 = pd.DataFrame({'col_first': [1,2,3],
                    'col_second': [4,5,6],
                    'col_theard': ['one', 'two', 'three']})

print(df1)
print(df1.pivot(index='col_theard', columns='col_first'))