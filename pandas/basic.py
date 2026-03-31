import pandas as pd

myDataset ={
    'cars' : ['BMW', 'AUDI', 'TOYOTA', 'HONDA'],
    'passings' : [3, 7, 2, 6]
}

myVar = pd.DataFrame(myDataset)

print(myVar)
