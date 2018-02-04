# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
import matplotlib.pyplot as plt
import sys
from parametros import *
from funcoes import *
#===============================================================================
# Melnikov Potential

def L( I_1 , I_2 , theta_1 , theta_2  , tau ):
    omega_1 , omega_2 = I_1 * Omega_1 , I_2 * Omega_2
    omega_3 = omega_1 + omega_2 -1
    l = A( a_1 , omega_1 ) * np.cos( theta_1 - omega_1 * tau  ) + A( a_2 , omega_2 ) * np.cos( theta_2 - I_2 * Omega_2 * tau ) + A( a_3 , omega_3 ) * np.cos( theta_1 + theta_2 - omega_3 * tau )
    return l

def part_der_L_I_1( I_1 , I_2 , theta_1 , theta_2 , tau):
    omega_1 , omega_2 = I_1 * Omega_1 , I_2 * Omega_2
    omega_3 = omega_1 + omega_2 -1
    der = Omega_1 * der_A( a_1 , omega_1) * np.cos(theta_1 - omega_1 * tau) + Omega_1 * A( a_1 , omega_1 ) * tau * np.sin( theta_1- omega_1 *tau )  + Omega_1 * der_A(a_3 , omega_3) * np.cos( theta_1 + theta_2 - omega_3 * tau ) + Omega_1 * A( a_3 , omega_3 ) * tau*np.sin( theta_1 + theta_2 - omega_3 * tau)
    return der

def part_der_L_I_2( I_1 , I_2 , theta_1 , theta_2 , tau):
    omega_1 , omega_2 = I_1 * Omega_1 , I_2 * Omega_2
    omega_3 = omega_1 + omega_2 -1
    der = Omega_2 * der_A( a_2 ,  omega_2 ) * np.cos( theta_2 - omega_2 * tau)  + Omega_2*A( a_2 , omega_2) * tau *np.sin(theta_2 - omega_2 * tau ) + Omega_2 * der_A( a_3 , omega_3 )*np.cos( theta_1 + theta_2 - omega_3 * tau) + Omega_2 * A(a_3 , omega_3) * tau * np.sin( theta_1 + theta_2 - omega_3 * tau)
    return der

def part_der_L_theta_1( I_1 , I_2 , theta_1 , theta_2  , tau ):
    omega_1 , omega_2 = I_1 * Omega_1 , I_2 * Omega_2
    omega_3 = omega_1 + omega_2 -1
    der = -A( a_1, omega_1 ) * np.sin( theta_1 - omega_1 * tau ) - A( a_3 , omega_3 ) * np.sin( theta_1 + theta_2 - omega_3 * tau)
    return der

def part_der_L_theta_2( I_1 , I_2 , theta_1 , theta_2 , tau) :
    omega_1 , omega_2 = I_1 * Omega_1 , I_2 * Omega_2
    omega_3 = omega_1 + omega_2 -1
    der = -A( a_2, omega_2 ) * np.sin( theta_2 - omega_2 * tau ) - A( a_3 , omega_3 ) * np.sin( theta_1 + theta_2 - omega_3 * tau )
    return der
#-------------------------------------------------------------------------------
