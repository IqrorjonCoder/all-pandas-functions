import pandas as pd

df1 = pd.DataFrame({
    'a': [True, None, False],
    'b': [6,7,8],
    'c': [60.12,7.32,8.65],
})

print(df1)
print(df1.to_parquet("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_pandas_functions1/base/df.parquet.gzip",
                     compression='gzip'))