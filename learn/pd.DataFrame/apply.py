import pandas as pd
import numpy as np

d = {
    'a': [-1, -2, -3, np.nan],
    'b': [1, 2, -3, 100],
}


def simple_f(x):
    return x + 1


data = pd.DataFrame(d)

print(data)
print(data.apply(simple_f))
