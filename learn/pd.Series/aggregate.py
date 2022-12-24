import pandas as pd

d = [1, 2, 3, None]

data = pd.Series(d)


def simplee_func(x):
    return x + 100


print(data)
print(data.aggregate(simplee_func))
