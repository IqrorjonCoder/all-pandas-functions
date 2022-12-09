import pandas as pd


d = {
    'a': [1,3,4,None,None],
    'b': [10,20,30,None,None],
    'c': [10,20,30,10,5],
}

data = pd.DataFrame(d)

print(data)
print(data.ewm(com=1))