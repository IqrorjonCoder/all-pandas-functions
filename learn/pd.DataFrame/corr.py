import pandas as pd


d = {
    'a': [1,2,3,4,2],
    'b': [10,20,30,2,1],
}

data = pd.DataFrame(d)

print(data)
print(data.corr())
