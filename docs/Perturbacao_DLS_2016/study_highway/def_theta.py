# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from func_f import *
from func_coeficientes import *
from parametros import *
#===============================================================================
def theta_H_1( I ):
    theta_1 = -np.arccos( A_3 * (1 - f_1( I ))/A(I , Omega_1 , a_1) ) - I * np.arccos(f_1(I))
    theta_H = theta_1 %( 2 * np.pi )
    return theta_H

def theta_H_2( I ):
    theta_2 = -np.arccos( A_3 * (1 - f_1( I ))/A(I , Omega_2 , a_2) ) - I * np.arccos(f_1(I))
    theta_H_b = theta_2 % (2 * np.pi )
    return theta_H_b
