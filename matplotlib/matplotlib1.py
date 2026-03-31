import matplotlib.pyplot as plt

x= [1,2,3,4,5]
y = [2,4,6,8,10]

# plt.plot(x,y)
# plt.show()

plt.plot(x,y)

# plt.xlabel("X values")
# plt.ylabel("y values")
# plt.show()

plt.plot(x,y, linestyle = ' ', marker='o')
plt.title("Customized line plot")
plt.show()


# plt.style.use("ggplot")
# plt.plot(x,y)
# plt.title("GGPlot Style Example")
# plt.show()