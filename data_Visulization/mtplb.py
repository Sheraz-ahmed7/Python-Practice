import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[6,7,8,9,10]

y2 = [2,3,4,5,6]

#plt.plot(x,y, linestyle='--', marker='o', color='r')  # Line style, marker, and color
plt.plot(x,y, label='Linear')
plt.plot(x,y2, label='Square')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

plt.show()