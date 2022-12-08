import pandas as pd
import numpy as np

d = {
    'a': [-1, -2, -3],
    'b': [1, 2, 3],
}


data = pd.DataFrame(d).align(other=pd.DataFrame({'c': [4,5,6],
                                                 'd': [7,8,9]}),
                             join="outer")

print(data)
