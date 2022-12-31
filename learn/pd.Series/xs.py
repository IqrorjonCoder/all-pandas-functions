import pandas as pd

d = [1,2,3,3]

data = pd.Series(d, index=['one', 'two', 'three', 'three2'])

print(data)
print(data.xs('one'))