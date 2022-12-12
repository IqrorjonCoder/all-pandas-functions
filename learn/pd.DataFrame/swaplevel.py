import pandas as pd

df1 = pd.DataFrame(
    {"Grade": ["A", "B", "A", "C"]},
    index=[
        ["Final exam", "Final exam", "Coursework", "Coursework"],
        ["History", "Geography", "History", "Geography"],
        ["January", "February", "March", "April"],
    ],
)

print(df1)
print(df1.swaplevel())