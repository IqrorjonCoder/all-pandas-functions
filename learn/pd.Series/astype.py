import numpy as np
import pandas as pd

d = [1,2,3,-100]

data = pd.Series(d)

print(data)
print(data.astype(dtype=np.int32))
print(data.astype(dtype=np.float32))