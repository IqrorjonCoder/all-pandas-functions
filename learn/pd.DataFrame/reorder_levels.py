import pandas as pd

df1 = pd.DataFrame({'a': [1,1,3,10],
                    'b': [4,5,6,10],
                    'c': [-10,-20,-30,-40]}).set_index(['a', 'b'])

print(df1)
print(df1.reorder_levels(['a', 'b']))