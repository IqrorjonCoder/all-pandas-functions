import pandas as pd


d = {
    'a': [1,2,None],
    'b': [10,None,30],
}

data = pd.DataFrame(d)

print(data)
print(data.combine_first(other=pd.DataFrame({'a': [100,200,300],
                                             'b': [1.1,2.2,3.3]})))