import pandas as pd
import numpy as np

d = [None, 1, 2, np.nan]

data = pd.Series(d)

print(data)
print(data.ffill())