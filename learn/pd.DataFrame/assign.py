import pandas as pd
import numpy as np

d = {
    'a': [1,2,3,np.nan],
    'b': [1,2,3,pd.NA],
}

data = pd.DataFrame(d)

print(data)
print(data.assign(c=lambda df:df.a+100,
                  d=lambda df:df.b+200))
