import pandas as pd
import numpy as np

d = {
    'a': ['2005-08-01','2005-08-11'],
    'b': ['2005-08-21', '2005-08-31'],
}

data = pd.DataFrame(d)

print(data)
print(data.asfreq(freq='10D'))
