import pandas as pd


d = {
    'a': [1,2,3],
    'b': [10,20,30],
}

data = pd.DataFrame(d)

print(data)
print(data.corrwith(pd.DataFrame({'a': [1.1,1.2,1.3],
                                  'b': [6,7,8]})))
