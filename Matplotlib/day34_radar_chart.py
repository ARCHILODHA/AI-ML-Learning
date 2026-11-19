import matplotlib.pyplot as plt
import numpy as np

categories = ["Python", "Java", "SQL", "ML", "Cloud"]

values = [8, 7, 9, 6, 8]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)

values += values[:1]
angles = np.append(angles, angles[0])

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})

ax.plot(angles, values, marker="o")
ax.fill(angles, values, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

ax.set_title("Skills Radar Chart")

plt.show()
