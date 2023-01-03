import pandas as pd

data = pd.Index([1,2,None,-100])

print(data)
print(data.is_categorical())
print(pd.CategoricalIndex([1,2,3]).is_categorical())