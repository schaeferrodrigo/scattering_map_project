# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
#import matplotlib.pyplot as plt
#import sys
from parametros import *
#==========================================================
#functions

def A( a , omega ):
    " funçoes coeficientes A_i"
    A = 2 * np.pi * omega * a/np.sinh(np.pi*omega/2)
    return A

def der_A( a , omega ):
    "derivada de A_i"
    der = 2 * np.pi * a * ( np.sinh( np.pi * omega / 2) - omega *(np.pi / 2)* np.cosh( np.pi * omega / 2)) /(np.sinh(np.pi * omega /2)**2)
    return der

#--------------------------------------------------------
#resonances of second order

def res_1( I ):
    ''' Omega * I = 1 '''
    res = I == 1
    return res

def res_2( I , J):
    ''' 2 * Omega_i * I  + Omega_j * J = 1'''
    res = 2 * I + J == 1
    return res    
