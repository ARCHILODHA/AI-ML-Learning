import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = np.linspace(-3,3,50)

X, Y = np.meshgrid(x,y)

Z = X**2 + Y**2

plt.contour(X, Y, Z)

plt.title("Contour Plot")

plt.show()
