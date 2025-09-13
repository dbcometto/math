# For Nonlinear Dynamics book (Self Learning)
# Exercise 3.5.4 -- see notebook
# 14 Aug 25

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plotting
from scipy.optimize import fsolve

# 3.1.5a
h_my = 1
k_my = 1
L0_my = 3

f = lambda x,h,k,L0: -k*x+k*L0*x/np.sqrt(x**2+h**2)

x= np.linspace(-5,5,100)

plt.figure()

xdvals = f(x,h_my,k_my,L0_my)
plt.plot(x,xdvals,label=f"({h_my},{k_my},{L0_my})")

plt.grid(True)
plt.axhline(0, color='black', linewidth=1)  # horizontal axis
plt.axvline(0, color='black', linewidth=1)  # vertical axis

plt.xlabel("x")
plt.ylabel(r"$\dot{x}$")
plt.title(r"$\dot{x}$ vs $x$ for a bead on a horizontal string where $h = 1$")
plt.legend()



# # showing x* as function of r

L0 = np.linspace(0,10,100)

X = [
    0*L0,
    np.sqrt(L0**2-h_my**2),
    -np.sqrt(L0**2-h_my**2)
]


# Next, determine stability
Xstab = []
X_stable = []
X_unstable = []

for i, x in enumerate(X):
    Xstab.append((-1+L0*h_my**2/(x**2+h_my**2)**(3/2)) <= 0)
    X_stable.append(np.where(Xstab[i], x, np.nan))
    X_unstable.append(np.where(~Xstab[i], x, np.nan))

# Then plot
plt.figure()

for x_stable, x_unstable in zip(X_stable, X_unstable):
    plt.plot(L0,x_stable,"k-",label="Stable")
    plt.plot(L0,x_unstable,"k--",label="Unstable")

plt.grid(True)
plt.axhline(0, color='black', linewidth=1)  # horizontal axis
plt.axvline(0, color='black', linewidth=1)  # vertical axis

plt.xlabel("L0")
plt.ylabel("x")
plt.title(r"Bifurcation Diagram for a bead on a horizontal string where $h = 1$")


# Fix duplicate legend entries
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())



# Show plots
plt.show()