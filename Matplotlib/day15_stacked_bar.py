import matplotlib.pyplot as plt

x = ["A","B","C"]
y1 = [3,5,7]
y2 = [2,4,6]

plt.bar(x, y1)
plt.bar(x, y2, bottom=y1)

plt.title("Stacked Bar")
plt.show()
