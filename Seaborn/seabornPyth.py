import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = sns.load_dataset('tips')

# df = sns.load_dataset('Iris')

# df = sns.load_dataset('titanic')
# print(df.head())

# sns.countplot(x='day', data=df)
# plt.show()


sns.scatterplot(x='total_bill', y='tip', hue = 'sex' , data=df)
plt.show()