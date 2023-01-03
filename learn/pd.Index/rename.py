import pandas as pd

data = pd.Index([1,2,3,None], name="simplee")

print(data)
print(data.rename(name="neww"))