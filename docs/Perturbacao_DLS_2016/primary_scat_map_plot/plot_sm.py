# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
import matplotlib.pyplot as plt
import sys
from parametros import *
from funcoes import *
from potencial_melnikov import *
from met_tau import *
from ponto_fixo import *
from scattering_map_function import *
from many_scattering_maps import *
import matplotlib.cm as cm
#===============================================================================
def plot_scattering_map(domain_I_1, domain_I_2 , domain_theta_1 , domain_theta_2 ):
    "plot de varias órbitas de Scattering map"
    I_1 , I_2 , theta_1 , theta_2 = many_scattering_maps(domain_I_1 , domain_I_2 ,domain_theta_1, domain_theta_2)
    keys = dict.keys(I_1)
    colors = cm.rainbow(np.linspace( 0,1 , len(keys) ))
    plt.figure()
    for key in keys:
        index = keys.index(key)
        plt.xlabel(r'$\theta_1$' , fontsize = 25)
        plt.ylabel('$I_1$' , fontsize = 25 , rotation = 'horizontal')
        plt.axis([0 , 2 * np.pi , -5 , 5 ])
        plt.plot( theta_1[key] , I_1[key]  , '.' , color = colors[ index ] , markersize = 0.7)
    plt.figure()
    for key in keys:
        index = keys.index( key )
        plt.xlabel(r'$\theta_2$' , fontsize = 25)
        plt.ylabel('$I_2$' , fontsize = 25 , rotation = 'horizontal')
        plt.axis([0 , 2 * np.pi , -5 , 5 ])
        plt.plot( theta_2[key] , I_2[key]  , '.' , color = colors[ index ] , markersize = 0.7)
    plt.figure()
    for key in keys:
        index = keys.index( key )
        plt.xlabel('$I_2$' , fontsize = 25)
        plt.ylabel('$I_1$' , fontsize = 25 , rotation = 'horizontal' )
        plt.axis([-5 , 5 , -5 , 5 ])
        plt.plot( I_2[key] , I_1[key]  , '.' , color = colors[ index ] , markersize = 0.7)
    plt.show()

plot_scattering_map(domain_I_1 , domain_I_2 , domain_theta_1, domain_theta_2 )
