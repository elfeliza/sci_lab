import numpy as np
from scipy.linalg import solve
from matplotlib import pyplot as plt

file = np.loadtxt('large.txt', skiprows=1)
N = file.shape[1]

matr = file[:N, :]

b = file[-1, :]

x = solve(matr, b)

plt.bar(range(x.shape[0]), x)
plt.savefig('p.png')
plt.show()