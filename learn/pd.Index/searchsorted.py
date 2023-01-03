import pandas as pd
import numpy as np

data = pd.Index([4,2,3,None,-100])

print(data)
print(data.searchsorted(np.array([4,3,2,-100])))