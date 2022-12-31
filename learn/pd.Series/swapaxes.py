import pandas as pd

d = [1,2,3,None]

data = pd.Series(d).rename_axis('simple')

print(data)
print(data.swapaxes.__doc__)