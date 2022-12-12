import pandas as pd

df1 = pd.DataFrame({
    'a': [True, True, False],
    'b': [6,7,8],
    'c': [60.12,7.32,8.65],
})

print(df1)
print(df1.sem())