import pandas as pd

d1 = {
    'a': [1,2,3],
    'b': [-10,20,-30],
}
d2 = {
    'b': [100,200,300],
    'c': [10,20,30],
}

data1 = pd.DataFrame(d1)
data2 = pd.DataFrame(d2)

print("data1:  \n", data1)
print("data2:  \n", data2)
data1.update(data2)
print("updated data: \n", data1)