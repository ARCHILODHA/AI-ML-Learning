import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axis('off')

table = ax.table(
    cellText=[[90,85],[88,92],[95,91]],
    rowLabels=['Alice','Bob','Charlie'],
    colLabels=['Math','Science'],
    loc='center'
)

table.scale(1,2)

plt.title("Table in Matplotlib")

plt.show()
