import pandas as pd

data = pd.Index([1,2,-100,None])

print(data)
print(data.is_object())
print(pd.Index(['one', 'two']).is_object())