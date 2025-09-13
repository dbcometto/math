# For Nonlinear Dynamics book (Self Learning)
# Exercise 3.6.5 -- see notebook
# 14 Aug 25

import numpy as np
import matplotlib.pyplot as plt

x0 = 1
y0 = 0
fx = lambda t,x,y: np.sin(x)
fy = lambda t,x,y: -np.cos(y)

t0 = 0
tend = 10
steps = 100
h = (tend-t0)/steps

# These are n
indexes = range(0, steps-1)

tvals = np.zeros(steps)
xvals = np.zeros(steps)
yvals = np.zeros(steps)

xvals[0] = x0
yvals[0] = x0


for i in indexes:
    t = tvals[i]
    x = xvals[i]
    y = yvals[i]

    k1 = fx(t,x,y)
    k2 = fx(t+h/2,x+h*k1/2,y)
    k3 = fx(t+h/2,x+h*k2/2,y)
    k4 = fx(t+h,x+h*k3,y)

    k5 = fy(t,x,y)
    k6 = fy(t+h/2,x,y+h*k5/2)
    k7 = fy(t+h/2,x,y+h*k6/2)
    k8 = fy(t+h,x,y+h*k7)

    tvals[i+1] = t + h
    xvals[i+1] = x + h/6*(k1+2*k2+2*k3+k4)
    yvals[i+1] = y + h/6*(k5+2*k6+2*k7+k8)
    



# Plot

plt.plot(xvals,yvals)

plt.grid(True)
plt.axhline(0, color='black', linewidth=1)  # horizontal axis
plt.axvline(0, color='black', linewidth=1)  # vertical axis

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Vector Field of System")
plt.legend()
plt.axis('equal')

# Show plots
plt.show()