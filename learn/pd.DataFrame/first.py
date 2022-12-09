import pandas as pd


d = {
    'a': [1,3,4,None],
    'b': [10,20,30,None],
    'c': [10,20,30,None],
}

data = pd.DataFrame(d).set_index(pd.date_range('1/1/2005', periods=4, freq='1D'))

print(data)
print(data.first('2D'))