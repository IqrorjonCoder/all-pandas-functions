import pandas as pd

d = [1.123, 2.234, 3.456]

data = pd.Series(d)

print(data)
print(data.round(2))