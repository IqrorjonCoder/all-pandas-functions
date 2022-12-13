import pandas as pd
import sqlite3

df1 = pd.DataFrame({
    'a': [True, None, False],
    'b': [6,7,8],
    'c': [60.12,7.32,8.65],
})

con = sqlite3.connect("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_pandas_functions1/base/simplee.sqlite3")

print(df1)
print(df1.to_sql(name="df", con=con))