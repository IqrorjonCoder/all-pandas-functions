import pandas as pd

d = [1,2,None,10]

data = pd.Series(d)

print(data)
data.to_latex("/home/iqrorjoon/PycharmProjects/pandas all functions/base/series_latex")