import pandas as pd


d = {
    'a': [1,2,3,4],
    'b': [10,20,30,40],
}

data = pd.DataFrame(d)

print(data)
print(data.drop(index=1))
print(data.drop(columns='a'))
print(data.drop(columns='a', index=0))