import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(
    np.arange(-2, 3, 1),
    np.arange(-2, 3, 1)
)

u = -y
v = x

plt.quiver(x, y, u, v, color="blue")

plt.title("Quiver Plot - Vector Field")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

plt.show()
