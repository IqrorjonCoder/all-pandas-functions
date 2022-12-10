import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame({'a': [1,2,3,None],
                    'b': [4,5,6,None]})

print(df1)
df1.plot()
plt.show()