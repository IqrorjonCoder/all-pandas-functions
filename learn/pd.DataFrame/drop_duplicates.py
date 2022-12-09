import pandas as pd


d = {
    'a': [1,3,4,6,6],
    'b': [10,20,30,6,6],
    'c': [10,20,30,10,5],
}

data = pd.DataFrame(d)

print(data)
print(data.drop_duplicates(subset=['a']))