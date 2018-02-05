# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
#===============================================================================
a_1 = 0.1 #coeficientes -- mu_1
a_2 = 0.3 #coeficientes -- mu_2
a_3 = 1.
Omega_1 = 1. # 'coeficiente' do I_1
Omega_2 = 1.  # 'coeficiente' do I_2
eps = 0.01   # epsilon da perturbaçao
#------------------------
max_steps = 50000 #número máximo de iteraçoes do scattering map
n_steps = 0 # contador de  passos
#-------------------------
#iv_I_1 =  0.1  #valor inicial de I_1
#iv_I_2 = 0.1  #valor inicial de I_2
#======================================
domain_theta_2 = np.linspace( np.pi , 3*np.pi/2 , 5 , endpoint = True ) #dominio de variaçao de theta_1 e theta_2
domain_theta_1 = np.linspace( np.pi , 3*np.pi/2 , 5 , endpoint = True )
domain_I_1 = np.linspace( 0.5 , 2. , 5. , endpoint = True)
domain_I_2 = np.linspace( 0.5 , 2. , 5. , endpoint = True)
