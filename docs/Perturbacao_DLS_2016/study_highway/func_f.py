# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from func_coeficientes import *
from parametros import *
#===============================================================================

def f_1( I ):
    fun_neg_1 = ( (I**2) * A_3 - np.sqrt(A_3**2 + ((I**2) - 1) * (I**2)*(A(I , Omega_1 , a_1)**2)) )/(((I**2) - 1)*A_3)
    return fun_neg_1

def f_2( I ):
    fun_neg_2 = ( (I**2) * A_3 - np.sqrt(A_3**2 + ((I**2) - 1) * (I**2)*(A(I , Omega_2 , a_2)**2)) )/(((I**2) - 1)*A_3)
    return fun_neg_2
