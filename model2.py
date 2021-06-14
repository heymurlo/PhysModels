import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

theta, phi = np.meshgrid(theta, phi)

xyz = np.array([np.sin(theta) * np.sin(phi),
                np.sin(theta) * np.cos(phi),
                np.cos(theta)])

def plot_Y(ax, el, m):

    Y = sph_harm(abs(m), el, phi, theta)

    if m < 0:
        Y = np.sqrt(2) * (-1) ** m * Y.imag
    elif m > 0:
        Y = np.sqrt(2) * (-1) ** m * Y.real
    Yx, Yy, Yz = np.abs(Y) * xyz


    cmap = plt.cm.ScalarMappable(cmap=plt.get_cmap('PRGn'))
    cmap.set_clim(-0.5, 0.5)

    ax.plot_surface(Yx, Yy, Yz,
                    facecolors=cmap.to_rgba(Y.real),
                    rstride=2, cstride=2)

    ax_lim = 0.5
    ax.plot([-ax_lim, ax_lim], [0, 0], [0, 0], c='0.5', lw=1, zorder=10)
    ax.plot([0, 0], [-ax_lim, ax_lim], [0, 0], c='0.5', lw=1, zorder=10)
    ax.plot([0, 0], [0, 0], [-ax_lim, ax_lim], c='0.5', lw=1, zorder=10)
    ax_lim = 0.5
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)
    ax.set_zlim(-ax_lim, ax_lim)
    ax.axis('off')


fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.add_subplot(projection='3d')
l, m = 3, 1

plot_Y(ax, l, m)
plt.show()