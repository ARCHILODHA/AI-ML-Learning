import numpy as np

names = np.array(["Archi", "NumPy", "Python"])

print(np.char.upper(names))

print(np.char.lower(names))

print(np.char.capitalize(names))

print(np.char.replace(names, "o", "0"))
