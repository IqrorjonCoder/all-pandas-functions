import pandas as pd

d = [1,10,100,2,20,None]

data = pd.Series(d)

print(data)
print(data.factorize())