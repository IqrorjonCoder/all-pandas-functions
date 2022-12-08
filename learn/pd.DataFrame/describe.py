import numpy as np
import pandas as pd


d = {
    'a': [1,2,3,None],
    'b': [10,20,30,None],
}

data = pd.DataFrame(d)

print(data)
print(data.describe())

