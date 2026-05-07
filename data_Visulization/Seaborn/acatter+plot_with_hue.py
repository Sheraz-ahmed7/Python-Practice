import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df.head()

sns.scatterplot(x='total_bill', y='tip', hue='sex', data=df)
plt.show()