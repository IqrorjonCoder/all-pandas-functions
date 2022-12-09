import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import hist

d = {
    'first': [1,2,3],
    'second': [10,20,30],
}

data = pd.DataFrame(d)

print(data)
data.hist(xlabelsize=15,
          ylabelsize=15,
          xrot=10,
          yrot=-10)
plt.show()