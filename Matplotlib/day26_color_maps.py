import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10,10)

plt.imshow(data, cmap='viridis')

plt.colorbar()

plt.title("Color Map Example")

plt.show()
