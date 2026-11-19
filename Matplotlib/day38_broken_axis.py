import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D", "E"]
values = [10, 12, 14, 85, 90]

fig, (ax1, ax2) = plt.subplots(
    2, 1,
    sharex=True,
    figsize=(7, 5),
    gridspec_kw={"height_ratios": [1, 2]}
)

ax1.bar(categories, values)
ax2.bar(categories, values)

ax1.set_ylim(80, 95)
ax2.set_ylim(0, 20)

ax1.spines["bottom"].set_visible(False)
ax2.spines["top"].set_visible(False)

ax1.tick_params(bottom=False, labelbottom=False)

ax1.set_title("Bar Chart with Broken Y Axis")
ax2.set_xlabel("Categories")
ax2.set_ylabel("Values")

plt.tight_layout()
plt.show()
