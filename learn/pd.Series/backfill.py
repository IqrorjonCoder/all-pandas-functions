import numpy as np
import pandas as pd

d = [1,2,3,np.nan]

data = pd.Series(d)

print(data)
print(data.backfill())