import pandas as pd

functions = [i for i in dir(pd) if i[0] != '_']

for i, j in enumerate(functions):
    print(f"{i}. pd.{j}()")