import matplotlib.pyplot as plt

data = [
    [20, 25, 30, 35, 40, 45, 50],
    [30, 35, 40, 45, 50, 55, 60],
    [15, 20, 25, 30, 35, 40, 45]
]

plt.boxplot(
    data,
    notch=True,
    patch_artist=True,
    showmeans=True,
    labels=["Class A", "Class B", "Class C"]
)

plt.title("Notched Box Plot")
plt.xlabel("Classes")
plt.ylabel("Marks")
plt.grid(axis="y", alpha=0.3)

plt.show()
