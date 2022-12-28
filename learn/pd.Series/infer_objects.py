import pandas as pd

d = [1,10,2,20]

data = pd.Series(d)

print(data)
print(data.infer_objects())