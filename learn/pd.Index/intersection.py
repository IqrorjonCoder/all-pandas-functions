import pandas as pd

data = pd.Index([1,1,2,None,None])

print(data)
print(data.intersection([1,2,100]))