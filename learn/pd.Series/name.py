import pandas as pd

d = [1,2,3,40]

data = pd.Series(d, name="simplee series")

print(data)
print(data.name)