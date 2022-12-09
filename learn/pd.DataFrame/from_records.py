import pandas as pd


d = [
    {'first': 1, 'second': 100},
    {'first': 2, 'second': 100},
    {'first': 3, 'second': 100},
]

data = pd.DataFrame()

print(data)
print(data.from_records(d))