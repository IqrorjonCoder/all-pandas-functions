import pandas as pd
import sqlite3

d = [1,2,None,10]

data = pd.Series(d)

print(data)
print(data.to_string(na_rep="nonee"))
print(type(data.to_string(na_rep="nonee")))