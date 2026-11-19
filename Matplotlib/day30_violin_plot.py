import matplotlib.pyplot as plt

data = [
    [45, 50, 55, 60, 65, 70, 75],
    [40, 48, 52, 58, 62, 68, 72],
    [50, 55, 60, 65, 70, 75, 80]
]

plt.violinplot(data, showmeans=True, showmedians=True)

plt.title("Violin Plot")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.xticks([1, 2, 3], ["Group A", "Group B", "Group C"])
plt.grid(axis="y", alpha=0.3)

plt.show()
