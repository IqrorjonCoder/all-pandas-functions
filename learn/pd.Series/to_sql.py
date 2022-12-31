import pandas as pd
import sqlite3

d = [1,2,None,10]

data = pd.Series(d)

print(data)
data.to_sql("series_sql", sqlite3.connect("/home/iqrorjoon/PycharmProjects/pandas all functions/base/series_sql"))