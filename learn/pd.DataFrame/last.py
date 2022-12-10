import pandas as pd

d = {
    'first': [1,2,3],
    'second': [10,20,30],
}

data = pd.DataFrame(d).set_index(pd.date_range('1/1/2005', periods=3, freq='1D'))

print(data)
print(data.last('1D'))