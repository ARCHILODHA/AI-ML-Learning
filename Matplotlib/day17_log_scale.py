import matplotlib.pyplot as plt

x = [1,10,100,1000]
y = [1,2,3,4]

plt.plot(x,y)
plt.xscale("log")

plt.title("Log Scale Plot")
plt.show()
