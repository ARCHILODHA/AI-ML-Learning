import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = np.array([10, 15, 13, 18, 20])

lower_error = [1, 2, 1, 2, 1]
upper_error = [2, 1, 3, 1, 2]

errors = [lower_error, upper_error]

plt.errorbar(
    x, y,
    yerr=errors,
    fmt="o-",
    capsize=5,
    label="Measurements"
)

plt.title("Asymmetric Error Bars")
plt.xlabel("Experiment")
plt.ylabel("Measured Value")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
