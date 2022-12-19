import pandas as pd

d = [1,2,3,4,-5,None]

data = pd.Series(d)

print(data)
print(data.add_prefix(prefix="PrefixX_"))