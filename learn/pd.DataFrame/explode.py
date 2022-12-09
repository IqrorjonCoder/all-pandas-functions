import pandas as pd


d = {
    'a': [1,3,4,None,None,None],
    'b': [10,20,30, [1,2,3], 100,200],
    'c': [10,20,30,None,None,None],
}

data = pd.DataFrame(d)

print(data)
print(data.explode('b'))