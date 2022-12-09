import pandas as pd

d = {
    'first': [1,2,3,None],
    'second': [10,20,30,None],
}

data = pd.DataFrame(d)

print(data)
print(data.gt(pd.DataFrame({
    'first': [1,1,3,None],
    'second': [1,1,3,None],
})))