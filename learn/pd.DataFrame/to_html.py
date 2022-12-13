import pandas as pd

df1 = pd.DataFrame({
    'a': [True, None, False],
    'b': [6,7,8],
    'c': [60.12,7.32,8.65],
})

print(df1)
print(df1.to_html("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/all_pandas_functions/base/simplee.html",
                  col_space=100,
                  header=True,
                  index=True,
                  justify='center',
                  max_cols=3,
                  max_rows=3,
                  show_dimensions=True,
                  decimal='./',
                  notebook=False,
                  border=10,
                  table_id='simplee_tablee',
                  render_links=False))