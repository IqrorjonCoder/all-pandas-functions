import pandas as pd


d = {
    'a': [1,2,None],
    'b': [10,None,30],
}

data = pd.DataFrame(d)

print(data)
print(data.copy())
