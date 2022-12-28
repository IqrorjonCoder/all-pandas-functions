import pandas as pd
import matplotlib.pyplot as plt

d = [1,2,10,20,30,3]

data = pd.Series(d)

print(data)
data.hist()
plt.show()