import pandas as pd
import os

functions = [i for i in dir(pd) if i[:1] != '_']

for i, v in enumerate(functions):
    print(i, v)

    os.mkdir(f"./{i} {v}")
    with open(f"././{i} {v}/{v.lower()}.ipynb", 'w') as f:
        pass
