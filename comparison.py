# For Nonlinear Dynamics book (Self Learning)
# To compare sqrt(-r) and r/2 for r<0
# 13 Aug 25

import numpy as np
import matplotlib.pyplot as plt


r = np.linspace(-5,0,50)
f1 = r+2*np.sqrt(-r)
f2 = 2*np.sqrt(-r)

# Plot
plt.plot(r,f1,label="f1")
#plt.plot(r,f2,label="f2")


plt.grid(True)
plt.axhline(0, color='black', linewidth=1)  # horizontal axis
plt.axvline(0, color='black', linewidth=1)  # vertical axis

plt.xlabel("r")
plt.ylabel("f(r)")
plt.title("Which is bigger?")
plt.legend()
plt.show()
