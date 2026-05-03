import matplotlib.pyplot as plt
import numpy as np

x= np.random.rand(50)  # Generate 50 random x values
y= np.random.rand(50)  # Generate 50 random y values

plt.figure(figsize=(8, 6))  # Set the figure size
plt.scatter(x,y)
plt.title('Scatter Plot Example')
plt.show()