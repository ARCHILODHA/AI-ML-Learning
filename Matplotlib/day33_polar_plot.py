import matplotlib.pyplot as plt
import numpy as np

angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)
values = [4, 6, 5, 7, 8, 6, 4, 5]

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})

ax.plot(angles, values, marker="o", linewidth=2)
ax.fill(angles, values, alpha=0.25)

ax.set_title("Polar Plot")
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

plt.show()
