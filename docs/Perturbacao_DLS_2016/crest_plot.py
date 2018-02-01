# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
#===============================================================================
#declaração das variáveis globais

a_1, a_2, a_3 = 0.1, .2 , 1.
Omega_1 , Omega_2 = 1. , 1
I_1 = 1.5
I_2 = 1.138 - I_1
mu_1  , mu_2 = a_1/a_3 ,  a_2/a_3


print 'mu_1 es', mu_1
print 'mu_2 es', mu_2
######################################################################
omega_1 =  Omega_1*I_1
omega_2 = Omega_2*I_2
omega_3 = omega_1 + omega_2 - 1

#-----------------------------------------------------------------·
def A( omega , a ):
    if omega != 0:
        A =  (2*np.pi*omega*a)/(np.sinh((omega*np.pi)/2))
    else:
        A = 4*a
    return A

##############################################################################
# 'projeçoes'

def f_1(x,y):
    """ valores da soma em relaçao a  phi_2 e phi_3 """
    f_1 = -(A(omega_2 , a_2)*omega_2*np.sin(x)+A(omega_3 , a_3)*omega_3*np.sin(y))/(A(omega_1 , a_1)*omega_1)
    return f_1

def f_2(x,y):
    """valores da soma em relaçao a phi_1 e phi_3"""
    f_2 = -(A( omega_1 , a_1 )*omega_1*np.sin(x)+A( omega_3 , a_3 )*omega_3*np.sin(y))/(A( omega_2 , a_2 )*omega_2)
    return f_2

def f_3(x,y):
    """valores da soma em relaçao a phi_1 e phi_2"""
    f_3 = -(A(omega_1 , a_1)*omega_1*np.sin(x)+A( omega_2 , a_2 )*omega_2*np.sin(y))/(A(omega_3 , a_3)* omega_3)
    return f_3


def plot_implicit(fn, bbox=(-2.5,2.5)):
    ''' create a plot of an implicit function
    fn  ...implicit function (plot where fn==0)
    bbox ..the x,y,and z limits of plotted interval'''
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 130) # resolution of the contour
    B = np.linspace(xmin, xmax, 130) # number of slices
    A1,A2 = np.meshgrid(A,A) # grid on which the contour is plotted

    for z in B: # plot contours in the XY plane
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z')
        # [z] defines the only level to plot for this contour for this value of z

    for y in B: # plot contours in the XZ plane
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y')

    for x in B: # plot contours in the YZ plane
        Y,Z = A1,A2
        X = fn(x,Y,Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x')

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)
    ax.set_xlabel(r'$\varphi_1$' , fontsize = 25)
    ax.set_ylabel(r'$\varphi_2$' , fontsize = 25 )
    ax.set_zlabel(r'$\sigma$', fontsize = 25  )
    ax.set_xticks(np.linspace( 0 , 2*np.pi , 5 ))
    ax.set_xticklabels( [ '0' , r'$\pi/2$' , r'$\pi$' , r'$3\pi/2$'] , fontsize = 15)
    ax.set_yticks(np.linspace( 0 , 2*np.pi , 5 ))
    ax.set_yticklabels( [ '0' , r'$\pi/2$' , r'$\pi$' , r'$3\pi/2$'] , fontsize = 15)
    ax.set_zticks(np.linspace( 0 , 2*np.pi , 5 ))
    ax.set_zticklabels( [ '0' , r'$\pi/2$' , r'$\pi$' , r'$3\pi/2$'] , fontsize = 15 )
    #save picture
    mu_1_name , mu_2_name , I_1_name , I_2_name = str(mu_1).replace(".","") , str(mu_2).replace(".","") ,str(I_1).replace(".","") , str(I_2).replace(".","")
    name_pic = 'mu1_'+ mu_1_name + '__mu2_' + mu_2_name + '__I1_' + I_1_name + '__I2_' + I_2_name+'.svg'
    plt.savefig(name_pic)
    plt.show()

def surface_crest(x,y,z):
    #print  A(omega_1 , a_1)*omega_1*np.sin(x)
    sur =  A(omega_1 , a_1)*omega_1*np.sin(x)+A(omega_2 ,a_2)*omega_2*np.sin(y)+A(omega_3 , a_3)*omega_3*np.sin(z)
    return sur

plot_implicit(surface_crest, bbox=(0,2*np.pi))
