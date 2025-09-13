# For Nonlinear Dynamics book (Self Learning)
# Exercise 3.6.5 -- see notebook
# 14 Aug 25

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 3.6.5a
a_my = 1
k_my = 3
L0_my = 3
m_my = 1
g = 9.81
theta_my = np.pi/2/10

f = lambda x,a,k,L0,m,theta: -k*x+k*L0*x/np.sqrt(x**2+a**2)+m*g*np.sin(theta)

x= np.linspace(-5,5,100)

plt.figure()

xdvals = f(x,a_my,k_my,L0_my,m_my,theta_my)
plt.plot(x,xdvals,label=f"({a_my},{k_my},{L0_my},{m_my},{theta_my:.2f})")

plt.grid(True)
plt.axhline(0, color='black', linewidth=1)  # horizontal axis
plt.axvline(0, color='black', linewidth=1)  # vertical axis

plt.xlabel("x")
plt.ylabel(r"$\dot{x}$")
plt.title(r"$\dot{x}$ vs $x$ for a bead on a horizontal string where $h = 1$")
plt.legend()



# Catastrophe Plot

N = 10
# mvals = np.linspace(0.5,5,N)
# kvals = np.linspace(0.5,10,N)
# avals = np.linspace(0.5,2.5,N)
# L0vals = np.linspace(0.5,2.5,N)
# thetavals = np.linspace(np.pi/8,-np.pi/8,N)
# xvals = np.linspace(-5,5,N)

# r = L0vals/avals
# h = -mvals*g/kvals/avals*np.sin(thetavals)
# u = xvals/avals

r = np.linspace(-5,5,N)
h = np.linspace(-5,5,N)
u = np.linspace(-5,5,N)

R,H,U = np.meshgrid(r,h,u)

SurfC = R*U-U*np.sqrt(1+U**2)+H*np.sqrt(1+U**2)

verts, faces, normals, values = measure.marching_cubes(SurfC, level=0,
                                                      spacing=(r[1]-r[0],
                                                               h[1]-h[0],
                                                               u[1]-u[0]))
verts[:,0] += r.min()  # shift X-axis
verts[:,1] += h.min()  # shift Y-axis
verts[:,2] += u.min()  # shift Z-axis

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Create triangular mesh
mesh = Poly3DCollection(verts[faces], facecolor='cyan', edgecolor='k', alpha=0.6)
ax.add_collection3d(mesh)

# Set axes limits
ax.set_xlim(R.min(), R.max())
ax.set_ylim(H.min(), H.max())
ax.set_zlim(U.min(), U.max())

ax.set_xlabel(r'$R = \frac{L_0}{a}$')
ax.set_ylabel(r'$h=-\frac{mg}{ka}\sin\theta$')
ax.set_zlabel(r'$u = \frac{x}{a}$')
plt.title('Catastrophe Surface for a bead on an angled wire')
plt.tight_layout()

# # Voxel Version
# SurfVoxels = np.abs(SurfC) < 0.02


# # Plot
# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111, projection='3d')

# # Use alpha blending for transparency
# ax.voxels(SurfVoxels, facecolors='cyan', edgecolor=None, alpha=0.5)

# ax.set_xlabel('R')
# ax.set_ylabel('H')
# ax.set_zlabel('U')
# plt.title('Catastrophe surface (voxels)')
# plt.show()





# # showing x* as function of r

# L0 = np.linspace(0,10,100)

# X = [
#     0*L0,
#     np.sqrt(L0**2-h_my**2),
#     -np.sqrt(L0**2-h_my**2)
# ]


# # Next, determine stability
# Xstab = []
# X_stable = []
# X_unstable = []

# for i, x in enumerate(X):
#     Xstab.append((-1+L0*h_my**2/(x**2+h_my**2)**(3/2)) <= 0)
#     X_stable.append(np.where(Xstab[i], x, np.nan))
#     X_unstable.append(np.where(~Xstab[i], x, np.nan))

# # Then plot
# plt.figure()

# for x_stable, x_unstable in zip(X_stable, X_unstable):
#     plt.plot(L0,x_stable,"k-",label="Stable")
#     plt.plot(L0,x_unstable,"k--",label="Unstable")

# plt.grid(True)
# plt.axhline(0, color='black', linewidth=1)  # horizontal axis
# plt.axvline(0, color='black', linewidth=1)  # vertical axis

# plt.xlabel("L0")
# plt.ylabel("x")
# plt.title(r"Bifurcation Diagram for a bead on a horizontal string where $h = 1$")


# # Fix duplicate legend entries
# handles, labels = plt.gca().get_legend_handles_labels()
# by_label = dict(zip(labels, handles))
# plt.legend(by_label.values(), by_label.keys())



# Show plots
plt.show()