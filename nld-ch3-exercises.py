# For Nonlinear Dynamics book (Self Learning)
# Exercises for Chapter 3
# 14 Aug 25

import numpy as np
import matplotlib.pyplot as plt


# 3.1.5a
# xd = r^2-x^2

f = lambda x,r: r**2 -x**2

rvals = [-2.5,-1.5,0,1,2]
xvals = np.linspace(-5,5,100)

plt.figure()
for r in rvals:
    xdvals = f(xvals,r)
    plt.plot(xvals,xdvals,label=f"r={r}")

plt.grid(True)
plt.axhline(0, color='black', linewidth=1)  # horizontal axis
plt.axvline(0, color='black', linewidth=1)  # vertical axis

plt.xlabel("x")
plt.ylabel(r"$\dot{x}")
plt.title("3.1.1")
plt.legend()

# showing x* as function of r

r = np.linspace(-5,5,100)
xpos = r
xneg = -r

# Next, determine stability
xposstab = (-2*xpos) <= 0
xnegstab = (-2*xneg) <= 0

xpos_stable = np.where(xposstab, xpos, np.nan)
xpos_unstable = np.where(~xposstab, xpos, np.nan)
xneg_stable = np.where(xnegstab, xneg, np.nan)
xneg_unstable = np.where(~xnegstab, xneg, np.nan)

# Then plot
plt.figure()

plt.plot(r,xpos_stable,"k-",label="Stable")
plt.plot(r,xpos_unstable,"k--",label="Unstable")
plt.plot(r,xneg_stable,"k-",label="Stable")
plt.plot(r,xneg_unstable,"k--",label="Unstable")

plt.grid(True)
plt.axhline(0, color='black', linewidth=1)  # horizontal axis
plt.axvline(0, color='black', linewidth=1)  # vertical axis

plt.xlabel("r")
plt.ylabel("x")
plt.title("3.1.5a Bifurcation Diagram")


# Fix duplicate legend entries
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())



# Show plots
plt.show()