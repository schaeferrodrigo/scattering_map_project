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
from theta_inicial import *
#===============================================================================
# iterates of scattering map

# initial values for theta-
iv_theta_1, iv_theta_2 =  3* np.pi/2 , 3 *np.pi/2

#tau star
iv_tau = assign_tau( iv_I_1 , iv_I_2 , iv_theta_1 , iv_theta_2 )
#orbits
I_1_values , I_2_values  , theta_1_values , theta_2_values = np.array([iv_I_1]) , np.array([iv_I_2]) , np.array([iv_theta_1]) , np.array([iv_theta_2])
#the value of the melnikov potential for the initial values
ref_value = L( iv_I_1 , iv_I_2 , iv_theta_1 , iv_theta_2 , iv_tau)
# difference of the values of the melnikov potential along the orbits
error_control = 0
theta_verification = []
resonances_test = [res_1(iv_I_1), res_1(iv_I_1) , res_2(iv_I_1 , iv_I_2) ,res_2(iv_I_2 , iv_I_1)]

while n_steps < max_steps and any(resonances_test) == False:
    theta , tau_int = sol_ponto_fixo( iv_I_1, iv_I_2 , iv_theta_1 , iv_theta_2)
    I_11 = iv_I_1 + eps * part_der_L_theta_1( iv_I_1 , iv_I_2, theta[0] , theta[1] , tau_int )
    I_12 = iv_I_2 + eps * part_der_L_theta_2( iv_I_1 , iv_I_2, theta[0] , theta[1] , tau_int )
    print 'valores de I = ' , I_11 , I_12
    tau_1 = assign_tau( I_11 , I_12, theta[ 0 ] , theta[1] )
    diff = np.abs( L(I_11 , I_12 , theta[0] , theta[1] , tau_1) - ref_value )
    I_1_values ,I_2_values  = np.append( I_1_values , [I_11] ) , np.append( I_2_values , [I_12 ] )
    theta_1_values ,theta_2_values = np.append( theta_1_values , theta[ 0 ] ) , np.append( theta_2_values , theta[ 1 ] )
    iv_I_1 , iv_I_2 = I_11 , I_12
    resonances_test = [res_1(iv_I_1), res_1(iv_I_1) , res_2(iv_I_1 , iv_I_2) ,res_2(iv_I_2 , iv_I_1)]
    iv_theta_1 , iv_theta_2 = theta
    n_steps += 1
    error_control = max( diff , error_control )
    print 'numero de passos = ' , n_steps
    print error_control

#print error_control

#===============================================================================
#plot dos pontos
# theta_1 x I_1
plt.figure()
plt.xlabel(r'$\theta_1$' , fontsize = 25)
plt.ylabel('$I_1$' , fontsize = 25 , rotation = 'horizontal')
plt.axis([0 , 2 * np.pi , -5 , 5 ])
plt.plot( theta_1_values , I_1_values  , '.' , color = 'blue' )
#theta_2 x I_2
plt.figure()
plt.xlabel(r'$\theta_2$' , fontsize = 25)
plt.ylabel('$I_2$' , fontsize = 25 , rotation = 'horizontal')
plt.axis([0 , 2 * np.pi , -5 , 5 ])
plt.plot( theta_2_values , I_2_values  , '.' , color = 'blue' )
# I_2 , I_1
plt.figure()
plt.xlabel('$I_2$' , fontsize = 25)
plt.ylabel('$I_1$' , fontsize = 25 , rotation = 'horizontal')
plt.axis([-5 , 5 , -5 , 5 ])
plt.plot( I_2_values , I_1_values  , '.' , color = 'blue' )
plt.tight_layout()
plt.show()
