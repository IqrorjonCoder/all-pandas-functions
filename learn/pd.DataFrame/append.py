import pandas as pd
import numpy as np

d = {
    'a': [-1, -2, -3, np.nan],
    'b': [1, 2, -3, 100],
}


data = pd.DataFrame(d)

print(data)
print(data.append(pd.DataFrame({'a': [10,20,30,40],
                                'b': [1,2,3,4]})))
