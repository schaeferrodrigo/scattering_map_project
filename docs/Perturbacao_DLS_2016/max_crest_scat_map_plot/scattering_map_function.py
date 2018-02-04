# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
#import matplotlib.pyplot as plt
#import sys
from parametros import *
from funcoes import *
from potencial_melnikov import *
from met_tau import *
from ponto_fixo import *
from theta_inicial import *
#===============================================================================
def SM( iv_theta_2 , n_steps = 0 , iv_I_1 = iv_I_1 , iv_I_2 = iv_I_2  ):
    "iteraçao de uma orbita do scattering map"
    iv_theta_1 = sol_theta_initial(iv_I_1 , iv_I_2 , 3*np.pi/2 , iv_theta_2)
    iv_tau = assign_tau( iv_I_1 , iv_I_2 , iv_theta_1 , iv_theta_2 )
    I_1_values , I_2_values  , theta_1_values , theta_2_values = np.array([iv_I_1]) , np.array([iv_I_2]) , np.array([iv_theta_1]) , np.array([iv_theta_2])
    ref_value = L( iv_I_1 , iv_I_2 , iv_theta_1 , iv_theta_2 , iv_tau)
    diff_values = np.array([ 0 ])
    while n_steps < max_steps and np.maximum(iv_I_1 , iv_I_2) > 0 :
        theta , tau_int = sol_ponto_fixo( iv_I_1, iv_I_2 , iv_theta_1 , iv_theta_2)
        I_11 = iv_I_1 + (-eps) * part_der_L_theta_1( iv_I_1 , iv_I_2, theta[0] , theta[1] , tau_int )
        I_12 = iv_I_2 + (-eps) * part_der_L_theta_2( iv_I_1 , iv_I_2, theta[0] , theta[1] , tau_int )
        tau_1 = assign_tau(I_11 , I_12, theta[ 0 ] , theta[1] )
        diff = np.abs(L(I_11 , I_12 , theta[0] , theta[1] , tau_1) - ref_value)
        I_1_values = np.append( I_1_values , [I_11] )
        I_2_values = np.append( I_2_values , [I_12 ] )
        theta_1_values = np.append( theta_1_values , theta[ 0 ] )
        theta_2_values = np.append( theta_2_values , theta[ 1 ] )
        diff_values = np.append( diff_values , [ diff ] )
        iv_I_1 , iv_I_2 = I_11 , I_12
        iv_theta_1 , iv_theta_2 = theta
        n_steps += 1
        print 'numero de passos = ' , n_steps
    if iv_I_1 >= 5. or iv_I_2 >= 5:
        print  theta_I_1_0 , theta_I_2_0
    max_error = np.amax( diff_values )
    #print 'erro = ' , max_error
    return np.array([I_1_values , I_2_values , theta_1_values , theta_2_values])
