import pandas as pd

data = pd.Index([1,2,100,None])

print(data)
print(data.format(na_rep="nan_XXX", formatter=lambda x:x+100))
print(data.format(na_rep="nan_XXX"))