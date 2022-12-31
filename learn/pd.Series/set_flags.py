import pandas as pd

d = [1,2,3,None]

data = pd.Series(d)

print(data.flags)
print(data.set_flags(allows_duplicate_labels=False).flags)