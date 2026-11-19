import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

X, Y = np.meshgrid(x, y)

U = -Y
V = X

plt.streamplot(
    X, Y, U, V,
    density=1.2,
    color=np.hypot(U, V),
    cmap="viridis"
)

plt.colorbar(label="Vector Magnitude")
plt.title("Stream Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()
