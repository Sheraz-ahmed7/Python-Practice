import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Generate 1000 random numbers from a normal distribution
plt.hist(data, bins=30, edgecolor='black')  # Create a histogram with 30 bins
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()