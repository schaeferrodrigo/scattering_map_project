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
