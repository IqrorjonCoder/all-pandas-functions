import pandas as pd

d = {
    'things': ['a', 'b', 'c'],
    'a': [1,2,3],
    'b': [4,5,6],
    'c': [7,8,9],
}

data = pd.DataFrame(d)

print(data)
print(data.lookup(data.index, data['things']))