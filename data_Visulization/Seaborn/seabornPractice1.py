import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df.head()

sns.countplot(x='day', data=df)
plt.show()