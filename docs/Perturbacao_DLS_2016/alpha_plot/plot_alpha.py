# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def alpha1( I_1 , I_2):
    omega_3 = I_1 + I_2 - 1
    sinh_part = np.sinh(omega_3 * np.pi/2)/np.sinh( I_1 * np.pi/2)
    quad_part = (I_1 / omega_3)**2
    alpha = quad_part * sinh_part
    return alpha


fig = plt.figure(facecolor = 'white')
ax = fig.gca(projection = '3d')

#data
step = 0.05
domain_I = np.linspace( -3.5 , 3.5, 7./step )
omega_1 , omega_2 = np.meshgrid( domain_I , domain_I )
grap_alpha = alpha1( omega_1, omega_2 )

surface = ax.plot_surface( omega_1 , omega_2 , grap_alpha )

#axis
ax.set_zlim3d( -150 , 250)
ax.zaxis.set_major_locator(LinearLocator(5))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
ax.set_xlim3d(-3.5 , 3.5)
ax.set_ylim3d( -3.5 , 3.5)
ax.set_xlabel(r'$\omega_1$' , fontsize = 25 )
ax.set_ylabel(r'$\omega_2$' , fontsize = 25 )
ax.set_title(r'Graph of $\alpha_1(I_1 , I_2)$')
plt.show()
