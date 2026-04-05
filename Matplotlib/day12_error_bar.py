import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,6]
error = [0.5, 1, 0.7]

plt.errorbar(x, y, yerr=error)
plt.show()
