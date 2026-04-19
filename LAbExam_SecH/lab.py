# Write a Python function called plot_sensor_data(time_steps, readings).
#1.Inside the function, use Matplotlib to create a scatter plot.
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sensor_data(time_steps, readings):
    plt.scatter(time_steps, readings)
    plt.xlabel('Time Steps')
    plt.ylabel('Readings')
    plt.title('Sensor Data')
    plt.show()

#Add a title "Sensor Readings Over Time" and label the axes "Time (s)" and "Value".
def plot_sensor_data(time_steps, readings):
    plt.scatter(time_steps, readings)
    plt.xlabel('Time (s)')
    plt.ylabel('Value')
    plt.title('Sensor Readings Over Time')
    plt.show()

#Use Seaborn to create a boxplot of the readings to show the distribution.

def plot_sensor_data(time_steps, readings):
    sns.boxplot(data=readings)
    plt.title('Distribution of Sensor Readings')
    plt.show()

#4.Call the function using: time = [0, 1, 2, 3, 4] and values = [10, 12, 11, 15, 14].
time = [0, 1, 2, 3, 4]
values = [10, 12, 11, 15, 14]
plot_sensor_data(time, values)


