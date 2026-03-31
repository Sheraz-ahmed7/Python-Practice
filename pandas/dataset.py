import pandas as pd

myDataset = {
    'cars': ["BMW", "AUDI", "Ford"],
    'passings': [3,2,5]
}

myvar = pd.DataFrame(myDataset)

print(myvar)

print("Data frame Shape: ",myvar.shape)