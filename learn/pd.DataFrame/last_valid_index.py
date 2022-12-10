import pandas as pd

d = {
    'first': [1,2,3,4],
    'second': [10,20,30,40],
}

data = pd.DataFrame(d)

print(data)
print(data.last_valid_index())