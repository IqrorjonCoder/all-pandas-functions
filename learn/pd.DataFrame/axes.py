import pandas as pd


d = {
    'a': [1.5,2.6,3],
    'b': [1,2.5,3],
}

data = pd.DataFrame(d)

print(data)
print(data.axes)
