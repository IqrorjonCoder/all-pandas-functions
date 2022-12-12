import pandas as pd

df1 = pd.DataFrame({
    'b': pd.arrays.SparseArray([6,7,8]),
})

print(df1)
print(df1.sparse.to_coo())
print(df1.sparse.to_dense())
