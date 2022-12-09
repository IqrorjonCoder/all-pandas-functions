import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]]).set_index([0, 1]).rename_axis(['a', 'b'])

df.columns = pd.MultiIndex.from_tuples([('c', 'e'), ('d', 'f')], names=['level_1', 'level_2'])

print(df)
print(df.droplevel('b'))