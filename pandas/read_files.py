import pandas as pd

# data = {
#     "ID": range(1, 11),
#     "Name": ["Ali", "Sara", "John", "Lina", "Omar", "Mona", "Zain", "Ayesha", "Nashit", "Hina"],
#     "Age": [20, 22, 19, 21, 23, 20, 22, 21, 24, 20],
#     "Marks": [85, 90, 88, 75, 92, 80, 89, 95, 78, 84]
# }

data = {
    "ID": range(1, 16),
    "Name": [
        "Ali", "Sara", "John", "Lina", "Omar",
        "Mona", "Zain", "Ayesha", "Nashit", "Hina",
        "Bilal", "Sana", "Usman", "Kiran", "Daniyal"
    ],
    "Age": [20, 22, 19, 21, 23, 20, 22, 21, 24, 20, 23, 19, 22, 21, 25],
    "Marks": [85, 90, 88, 75, 92, 80, 89, 95, 78, 84, 91, 73, 87, 82, 94]
}

df = pd.DataFrame(data)
print(df)