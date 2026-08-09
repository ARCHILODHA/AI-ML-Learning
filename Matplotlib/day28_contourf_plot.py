import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = np.linspace(-3,3,50)

X, Y = np.meshgrid(x,y)

Z = np.sin(X) * np.cos(Y)

plt.contourf(X, Y, Z, cmap='plasma')

plt.colorbar()

plt.title("Filled Contour Plot")

plt.show()
