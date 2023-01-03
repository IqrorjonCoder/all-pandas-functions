import pandas as pd

data = pd.Index([1,2,None])

print(data)
print(data.set_value.__doc__)