import pandas as pd

d = [1,2,3,None]

data = pd.Series(d)

print(data)
print(data.transform(lambda x: x+100))