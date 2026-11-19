import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

x = np.random.randn(1000)
y = 2 * x + np.random.randn(1000)

plt.hexbin(x, y, gridsize=30, cmap="viridis", mincnt=1)

plt.colorbar(label="Point Density")
plt.title("Hexbin Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
