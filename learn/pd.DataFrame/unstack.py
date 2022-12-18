import pandas as pd

d = {
    'a': [1,2,3],
    'b': [-10,20,-30],
}

data = pd.DataFrame(d)

print(data)
print(data.unstack())