import pandas as pd


d = {
    'a': [1,2,3],
    'b': [10,20,30],
}

data = pd.DataFrame(d)

print(data)
print(data.combine(other=pd.DataFrame({'a': [10,20,30],'b': [1,2,3]}),
                   func=lambda df1, df2: df1 if df1.sum()>df2.sum() else df2))