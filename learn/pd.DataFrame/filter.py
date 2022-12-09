import pandas as pd


d = {
    'a': [1,3,4,None],
    'b': [10,20,30,None],
    'c': [10,20,30,None],
}

data = pd.DataFrame(d)

print(data)
print(data.filter(items=['a', 'c']))
print(data.filter(regex="a$", axis=1))
print(data.filter(like="1", axis=0))