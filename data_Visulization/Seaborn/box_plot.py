import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df.head()

sns.boxplot(x='day', y='total_bill', data=df)
plt.show()