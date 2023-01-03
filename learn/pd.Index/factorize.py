import pandas as pd

data = pd.Index([1,2,3,100,None])

print(data)
print(data.factorize())
print(data.factorize()[0])
print(data.factorize()[1])