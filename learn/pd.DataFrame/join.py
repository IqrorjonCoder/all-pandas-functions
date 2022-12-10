import pandas as pd

d = {
    'first': [1,2,3,None],
    'second': [10,20,30,None],
}

data = pd.DataFrame(d)

print(data)
data = data.join(pd.DataFrame({'c': [10,20,30,40]}), lsuffix='_caller', rsuffix='_other')
print(data)