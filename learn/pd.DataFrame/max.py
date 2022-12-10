import pandas as pd

d = {
    'first': [1,2,3,None],
    'second': [10,20,30,None],
}

data = pd.DataFrame(d)

print(data)
print(data.max())