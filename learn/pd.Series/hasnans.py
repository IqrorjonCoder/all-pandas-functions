import pandas as pd
import numpy as np

print(pd.Series([1,2]).hasnans)
print(pd.Series([1,2,None]).hasnans)
print(pd.Series([1,2,np.nan]).hasnans)