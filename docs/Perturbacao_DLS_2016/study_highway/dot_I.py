# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from def_theta import *
from parametros import *
from func_coeficientes import *
#===============================================================================
def dot_I_1( I,theta, tau):
    dot_I = -A(I , Omega_1 , a_1 ) * np.sin(theta - Omega_1 * I * tau)
    return dot_I

def dot_I_2( I , theta , tau ):
    dot_I = -A(I , Omega_2 , a_2 ) * np.sin(theta - Omega_2 * I * tau)
    return dot_I

def dot_theta_1( I, theta , tau ):
    dot_theta = - Omega_1 * ( der_A( I , Omega_1 , a_1) * np.cos( theta - Omega_1 * I * tau) + tau * A(I , Omega_1 , a_1) * np.sin( theta - Omega_1 * I * tau) )
    return dot_theta

def dot_theta_2( I , theta , tau ):
    dot_theta = - Omega_2 * ( der_A(I , Omega_2 , a_2) * np.cos( theta - Omega_2 * I * tau ) + tau * A(I , Omega_2 , a_2) * np.sin( theta - Omega_2 * I * tau ))
    return dot_theta
