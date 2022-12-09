import pandas as pd

d = {
    'first': [1,2,3],
    'second': [10,20,30],
}

data = pd.DataFrame(d)

print(data)
print(data.iat)
