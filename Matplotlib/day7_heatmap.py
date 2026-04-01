import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(5,5)

plt.imshow(data)
plt.colorbar()
plt.show()
