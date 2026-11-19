import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

x = np.random.normal(50, 10, 500)
y = 2 * x + np.random.normal(0, 15, 500)

fig = plt.figure(figsize=(8, 8))

grid = fig.add_gridspec(
    2, 2,
    width_ratios=(4, 1),
    height_ratios=(1, 4),
    hspace=0.05,
    wspace=0.05
)

ax_main = fig.add_subplot(grid[1, 0])
ax_top = fig.add_subplot(grid[0, 0], sharex=ax_main)
ax_right = fig.add_subplot(grid[1, 1], sharey=ax_main)

ax_main.scatter(x, y, alpha=0.6)
ax_top.hist(x, bins=25)
ax_right.hist(y, bins=25, orientation="horizontal")

ax_top.tick_params(labelbottom=False)
ax_right.tick_params(labelleft=False)

ax_main.set_xlabel("X Values")
ax_main.set_ylabel("Y Values")

fig.suptitle("Joint Distribution Plot")

plt.show()
