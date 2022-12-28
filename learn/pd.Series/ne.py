import pandas as pd

d = [1,2,3,40]

data = pd.Series(d)

print(data)
print(data.ne([-10,20,30,40]))