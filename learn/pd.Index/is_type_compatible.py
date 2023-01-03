import pandas as pd
import numpy as np

data = pd.Index([1,2,3,None,-100])

print(data)
print(data.is_type_compatible.__doc__)