import pandas as pd


d = {
    'a': [1.5,2.6,3],
    'b': [1,2.5,3],
}

data = pd.DataFrame(d).set_index(pd.date_range('1/1/2005', periods=3, freq='1H'))

print(data)
print(data.at_time('01:00'))


