import pandas as pd

df1 = pd.DataFrame({
    'a': [1,2,3,4,5],
    'b': [6,7,8,0,20],
})*10.123

print(df1)
print(df1.rpow(10))