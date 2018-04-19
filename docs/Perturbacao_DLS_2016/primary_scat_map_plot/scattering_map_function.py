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
import sys
#===============================================================================
def SM( PS , iv_I_1 , iv_I_2 , iv_theta_1 , iv_theta_2 , n_steps = 0  ):
    "iteraçao de uma orbita do scattering map.  PS = poincaré section. PS = 0 : wihtout Poincaré section (default) , PS != 0 with Poincaré section."
    verification = 0
    iv_tau = assign_tau( iv_I_1 , iv_I_2 , iv_theta_1 , iv_theta_2 )
    #orbits
    I_1_values , I_2_values  , theta_1_values , theta_2_values = np.array([iv_I_1]) , np.array([iv_I_2]) , np.array([iv_theta_1]) , np.array([iv_theta_2])
    ref_value = L( iv_I_1 , iv_I_2 , iv_theta_1 , iv_theta_2 , iv_tau)
    diff_values = np.array([ 0 ])
    resonances_test = [res_1(iv_I_1), res_1(iv_I_1) , res_2(iv_I_1 , iv_I_2) ,res_2(iv_I_2 , iv_I_1)] # set of resonances of second order
    while n_steps < max_steps and  any(resonances_test) == False:
        theta , tau_int = sol_ponto_fixo( iv_I_1, iv_I_2 , iv_theta_1 , iv_theta_2)
        I_11 = iv_I_1 + eps * part_der_L_theta_1( iv_I_1 , iv_I_2, theta[0] , theta[1] , tau_int )
        I_12 = iv_I_2 + eps * part_der_L_theta_2( iv_I_1 , iv_I_2, theta[0] , theta[1] , tau_int )
        tau_1 = assign_tau(I_11 , I_12, theta[ 0 ] , theta[1] )
        diff = np.abs(L(I_11 , I_12 , theta[0] , theta[1] , tau_1) - ref_value)
        if PS == 0:
            #print PS
            sys.exit('wrong buckle')
            I_1_values = np.append( I_1_values , [I_11] )
            I_2_values = np.append( I_2_values , [I_12 ] )
            theta_1_values = np.append( theta_1_values , theta[ 0 ] )
            theta_2_values = np.append( theta_2_values , theta[ 1 ] )
        else:
            #print 'here'
            if np.abs( theta[1] - np.pi) < 1e-3: #Poincaré section
                I_1_values = np.append( I_1_values , [I_11] )
                I_2_values = np.append( I_2_values , [I_12 ] )
                theta_1_values = np.append( theta_1_values , theta[ 0 ] )
                theta_2_values = np.append( theta_2_values , theta[ 1 ] )
                verification += 1
            else:
               pass
        #diff_values = np.append( diff_values , [ diff ] )
        iv_I_1 , iv_I_2 = I_11 , I_12
        iv_theta_1 , iv_theta_2 = theta
        n_steps += 1
        print 'numero de passos = ' , n_steps
    #print len(theta_2_values) , verification
    #print 'erro = ' , max_error
    return np.array([I_1_values , I_2_values , theta_1_values , theta_2_values])
