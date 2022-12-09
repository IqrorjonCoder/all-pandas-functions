import pandas as pd


d = {
    'a': [1,3,4,None],
    'b': [10,20,30,None],
    'c': [10,20,30,None],
}

data = pd.DataFrame(d)

print(data)
print(data.first_valid_index())