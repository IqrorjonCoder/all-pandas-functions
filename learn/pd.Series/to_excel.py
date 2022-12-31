import pandas as pd

d = [1,2,None,10]

data = pd.Series(d)

print(data)
data.to_excel("/home/iqrorjoon/PycharmProjects/pandas all functions/base/series_excel.xls")