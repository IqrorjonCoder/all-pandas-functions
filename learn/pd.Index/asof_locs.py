import pandas as pd
import numpy as np

data = pd.Index([1,2,3,100])

print(data)
print(data.asof_locs(pd.Index([-1,0,1,2,3,4]), mask=np.array([True, True, True, True])))