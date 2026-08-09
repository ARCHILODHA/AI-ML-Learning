import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.step(x, y, where='mid')

plt.title("Step Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)

plt.show()
