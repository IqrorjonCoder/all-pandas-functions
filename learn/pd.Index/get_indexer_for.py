import pandas as pd

data = pd.Index([1,2,None,100], name="simplee")

print(data)
print(data.get_indexer_for([1,2,3,100]))
print(data.get_indexer_for([1,2,None,100]))