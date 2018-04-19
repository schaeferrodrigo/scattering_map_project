# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
#===============================================================================
def A( I , Omega , a ):
    coef_1 = 2 * np.pi * a * I * Omega /np.sinh(np.pi * I * Omega/2)
    return coef_1

A_3 = 2 * np.pi/np.sinh( np.pi/2 )


def der_A(I , Omega , a):
    der_A = 2 * np.pi * a * Omega *  ( np.sinh( np.pi * I * Omega /2 ) - (I * Omega * np.pi/2 ) * np.cosh( np.pi * I * Omega/2 ))/(np.sinh(np.pi * Omega * I/2)**2)
    return der_A
