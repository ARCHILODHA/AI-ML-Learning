import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [5,3,7,2,6,4]

plt.stem(x, y)

plt.title("Stem Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
