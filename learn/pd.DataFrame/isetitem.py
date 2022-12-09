import pandas as pd

d = {
    'first': [1,2,3],
    'second': [10,20,30],
}

data = pd.DataFrame(d)

print(data)
data.isetitem(0, 200)
print(data)