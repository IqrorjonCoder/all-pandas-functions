import pandas as pd

data = pd.Index([200,1,2,3,100])

print(data)
print(data[data.argsort()])