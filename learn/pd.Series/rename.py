import pandas as pd

d = [1,2,300]

data = pd.Series(d, name="simplee")

print(data.name)
print(data.rename('x_iii').name)