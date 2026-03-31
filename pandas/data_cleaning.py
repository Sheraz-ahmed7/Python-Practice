import pandas as pd

data = {
    "Name": ["Ali", " Ahmed ", "Sara", "Ali", None],
    "Age": [20, -5, 150, 20, None],
    "Marks": [85, 90, None, 85, 200]
}

df = pd.DataFrame(data)
print(df)
