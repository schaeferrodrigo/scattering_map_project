# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from functions import *

def function_f(I):
    num = (I**2)*A(-1,a_2)-np.sqrt(A(-1,a_2)**2 +(I**2-1)*(I**2)*A(I,a_1)**2)
    den = (I**2 - 1) * A(-1,a_2)**2
    return num/den

def tau_highways(I):
     if I < 0:
         tau_h = -np.arccos(function_f(I))
         tau_H = np.arccos(function_f(I))
     else:
         tau_h = np.arccos(function_f(I))
         tau_H = - np.arccos(function_f(I))
    return [tau_h , tau_H]

def theta_highways(I):
    pass
    
