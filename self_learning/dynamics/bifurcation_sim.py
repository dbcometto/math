# For Nonlinear Dynamics book (Self Learning)
# To compare sqrt(-r) and r/2 for r<0
# 13 Aug 25

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Data
r0 = -1

x = np.linspace(-10, 10, 500)

# Plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # make room for slider
line, = ax.plot(x, x**2)

# Slider axis: [left, bottom, width, height]
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax=ax_slider, label='r', valmin=-10, valmax=10, valinit=r0)
slider.ax.autoscale(True)

line.ax.set_ylim(-10,10)
line.ax.autoscale(False)
line.plt.grid(True)
line.plt.axhline(0, color='black', linewidth=1)  # horizontal axis
line.plt.axvline(0, color='black', linewidth=1)  # vertical axis

# Update function
def update(val):
    r = slider.val
    line.set_ydata(r + x**2)
    fig.canvas.draw_idle()

slider.on_changed(update)




plt.show()
