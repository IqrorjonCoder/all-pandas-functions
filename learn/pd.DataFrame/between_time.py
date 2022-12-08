import pandas as pd


d = {
    'a': [1.5,2.6,3, None],
    'b': [1,2.5,3, None],
}

data = pd.DataFrame(d).set_index(pd.date_range('1/1/2005', periods=4, freq='1H'))

print(data)
print(data.between_time('1:00', '2:00'))

