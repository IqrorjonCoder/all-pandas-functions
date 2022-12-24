import pandas as pd

d = [1, 2, 3, None]

data = pd.Series(d)


def simple_func(x):
    return x * 100


print(data)
print(data.agg(simple_func))
