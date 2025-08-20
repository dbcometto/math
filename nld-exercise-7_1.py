# For Nonlinear Dynamics book (Self Learning)
# Exercise 3.6.5 -- see notebook
# 14 Aug 25

import numpy as np
import matplotlib.pyplot as plt

tol = 1e-5
values = 100
arrows = 25
step = values // arrows

# 3.6.5a
xvals = np.linspace(-10,10,values)
yvals = np.linspace(-10,10,values)

x,y = np.meshgrid(xvals,yvals)

r = np.sqrt(x**2+y**2)
theta = np.arctan2(y,x)

rdot = r*np.sin(r)
thetadot = 1*r**0

xdot = rdot*np.cos(theta) - r*np.sin(theta)*thetadot
ydot = rdot*np.sin(theta) + r*np.cos(theta)*thetadot

mags = np.sqrt(xdot**2+ydot**2)
mags[mags==0] = tol

u = xdot/mags
v = ydot/mags

plt.figure()

plt.contour(x,y,xdot,levels=[0], colors='r')
plt.contour(x,y,ydot,levels=[0], colors='b')
plt.contour(x,y,rdot,levels=[0], colors='orange')
plt.contour(x,y,thetadot,levels=[0], colors='cyan')

plt.quiver(x[::step, ::step],y[::step, ::step],u[::step, ::step],v[::step, ::step])

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