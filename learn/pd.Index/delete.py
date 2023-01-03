import pandas as pd

data = pd.Index([1,2,3,100])

print(data)
print(data.delete([0,1]))