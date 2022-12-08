import pandas as pd
import numpy as np

d = {
    'a': [-1, -2, -3],
    'b': [1, 2, 3],
}


def simplee(x):
    return x ** 2


data = pd.DataFrame(d).aggregate(simplee)

print(data)
