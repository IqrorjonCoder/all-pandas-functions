import pandas as pd

d = [1,2,3,40]

data = pd.Series(d)

print(data)
print(data.multiply([-10,20,-30,4]))