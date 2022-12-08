import pandas as pd

d = {
    'a': [-1,-2,-3],
    'b': [1,2,3],
}

data = pd.DataFrame(d).abs()

print(data)