from scipy.integrate import odeint
import numpy as np
import sympy as sym
from sympy.abc import x
from matplotlib import pyplot as plt

f = sym.Function('f')

res = sym.dsolve(f(x).diff(x) + 2 * f(x), f(x), ics={f(0): sym.sqrt(2)})

X = np.arange(0, 10, 0.1)
Y0 = [float(res.args[1].subs(x, i)) for i in X]

def dydt(y, t):
    return -2 * y

yyy = float(sym.sqrt(2))
Y = np.array(odeint(dydt, yyy, X)).flatten()

fig, axes = plt.subplots(3)
axes[0].plot(X, Y0, color='magenta', label='Sympy')
axes[1].plot(X, Y, color='pink', label='Scipy')
axes[0].legend()
axes[1].legend()


axes[2].plot(X, abs(Y-Y0))
axes[2].set_title('Difference (abs)')

plt.subplots_adjust(hspace=0.7)
plt.savefig('p.png')
plt.show()