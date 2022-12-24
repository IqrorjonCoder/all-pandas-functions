import pandas as pd

d = [1,2,3,None]

data = pd.Series(d)

print(data)
print(data.apply(lambda x: x*100))