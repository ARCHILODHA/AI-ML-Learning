import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,3,5,4,6]
y2 = [1,2,2,3,4]

plt.plot(x, y1)
plt.plot(x, y2)

plt.fill_between(x, y1, y2, alpha=0.3)

plt.title("Fill Between Curves")

plt.show()
