# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from parametros import *
from func_coeficientes import *
#===============================================================================

def Red_Poinc_function( I_1 , I_2, theta_1 , theta_2 , tau):
    red = A(I_1 , Omega_1 , a_1) * np.cos( theta_1  - Omega_1*I_1 * tau) + A(I_2 , Omega_2 , a_2) * np.cos( theta_2 - Omega_2 *I_2* tau) + A_3 * np.cos(-tau)
    return red


def eq_crest(  I_1 , I_2, theta_1 , theta_2 , tau):
    crista = Omega_1 * I_1*A(I_1,Omega_1 , a_1) * np.sin(theta_1 - Omega_1 * I_1 * tau) + Omega_2 * I_2 * A( I_2 , Omega_2, a_2 ) * np.sin( theta_2 - Omega_2 * I_2 * tau) + A_3 * np.sin(-tau)
    return crista
