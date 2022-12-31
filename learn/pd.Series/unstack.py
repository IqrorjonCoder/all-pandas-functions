import pandas as pd

s = pd.Series([1, 2, 3, 4],
              index=pd.MultiIndex.from_product([['one', 'two'],
                                                ['a', 'b']]))

print(s)
print(s.unstack())