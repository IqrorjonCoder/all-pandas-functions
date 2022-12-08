import pandas as pd


d = {
    'a': [1,2,3,4],
    'b': [10,20,30,40],
}

data = pd.DataFrame(d)

print(data)
print(data.div(2))