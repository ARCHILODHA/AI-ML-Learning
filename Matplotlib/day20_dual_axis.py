import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [200, 250, 300, 280, 350]
profit = [20, 25, 40, 35, 50]

fig, ax1 = plt.subplots()

ax1.plot(months, sales, marker='o')
ax1.set_xlabel("Months")
ax1.set_ylabel("Sales")

ax2 = ax1.twinx()
ax2.plot(months, profit, marker='s')
ax2.set_ylabel("Profit")

plt.title("Dual Axis Plot")
plt.show()
