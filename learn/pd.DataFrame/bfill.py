import pandas as pd


d = {
    'a': [1.5,2.6,3, None],
    'b': [1,2.5,3, None],
}

data = pd.DataFrame(d)

print(data)
print(data.bfill())