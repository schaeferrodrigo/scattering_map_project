# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from functions import *
import matplotlib.pyplot as plt
from parametros import *
#===============================================================================

def function_f(I):
    num = (I**2)*A(-1,a_2)-np.sqrt(A(-1,a_2)**2 +(I**2-1)*(I**2)*A(I,a_1)**2)
    den = (I**2 - 1) * A(-1,a_2)
    return num/den

def tau_highways(I):
    if I < 0:
        tau_h = -np.arccos(function_f(I))
        tau_H = np.arccos(function_f(I))
    else:
        tau_h = np.arccos(function_f(I))
        tau_H = - np.arccos(function_f(I))
    return [tau_h , tau_H]

def theta_h(I):
    num,den = A(-1,a_2)*(1-function_f(I)),A(I,a_1)
    main_part = np.arccos(num/den)
    theta = main_part + np.sign(I)*I*np.arccos(function_f(I))
    return theta

def theta_H(I):
    num,den = A(-1,a_2)*(1-function_f(I)), A(I,a_1)
    main_part = np.arccos(num/den)
    theta = -main_part -np.sign(I) *I*np.arccos(function_f(I))
    return (theta)%(2*np.pi)


domain_I = np.array(domain_I)
#
plt.plot( theta_H(domain_I),domain_I)
plt.plot(theta_h(domain_I),domain_I)
plt.axis([0,2*np.pi,-5,5])
plt.show()

print( A(-1,a_2)*(1-function_f(domain_I)))
print(A(domain_I,a_1))
print(theta_H(domain_I))
