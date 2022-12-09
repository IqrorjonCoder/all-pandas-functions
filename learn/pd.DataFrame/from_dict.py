import pandas as pd


d = {
    'a': [1,3,4,None],
    'b': [10,20,30,None],
    'c': [10,20,30,None],
}

data = pd.DataFrame()

print(data)
print(data.from_dict(d))
print(data.from_dict(d, orient='index'))
print(data.from_dict(d, orient='index', columns=['one', 'two', 'three', 'four']))