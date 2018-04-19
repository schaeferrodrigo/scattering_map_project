# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from RPF_and_crista import *
import sys
#===============================================================================
def bissec_method( I_1, I_2 , theta_1 , theta_2, tau_1 , tau_2  , tol = 1e-2 ):
    while np.abs( tau_1 - tau_2 ) > tol:
        tau_c = ( tau_1 + tau_2 )/2
        if eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_1 ) * eq_crest( I_1 , I_2 ,theta_1 , theta_2,  tau_c) < 0:
            tau_2 = tau_c
        else:
            tau_1 = tau_c
    return [tau_1 , tau_2]

def secant_method( I_1 , I_2 , theta_1 , theta_2, tau_1 , tau_2 ,tol = 1e-10):
    tau_sec = tau_1 - eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_1 )*( tau_1 - tau_2)/(eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_1) - eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_2) )
    while np.abs( eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_sec ) ) > tol:
        if eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_1 ) * eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_sec ) < 0 :
            tau_2  = tau_sec
        else:
            tau_1 = tau_sec
        tau_sec =  tau_1 - eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_1)*( tau_1 - tau_2)/(eq_crest( I_1, I_2 , theta_1 , theta_2,  tau_1 ) - eq_crest( I_1, I_2 , theta_1 , theta_2,  tau_2) )
    return tau_sec

def tau1( I_1 , I_2 ,theta_1,theta_2 ,sign , tau_initial = 0 , step = 0.05):
    tau_2 = tau_initial
    if sign == 'neg':
        tau_1 = -step
    else:
        tau_1 = step
    sign = np.sign(tau_1)
    while eq_crest( I_1 , I_2 , theta_1 , theta_2,  tau_1) * eq_crest( I_1, I_2 , theta_1 , theta_2,  tau_2 ) > 0 :
        tau_2 = tau_1
        tau_1 = tau_1 + sign * step
    candidate = bissec_method( I_1 , I_2 , theta_1 , theta_2 , tau_1 , tau_2  )
    tau_1 = candidate[0]
    tau_2 = candidate[1]
    tau_star = secant_method( I_1 , I_2 , theta_1 , theta_2 , tau_1 , tau_2 ) #método secante
    return tau_star

def assign_tau( I_1 , I_2, theta_1,theta_2):
    value_of_tau_pos = tau1( I_1, I_2, theta_1 , theta_2 , 'pos' )
    value_of_tau_neg = tau1( I_1 , I_2 , theta_1 , theta_2 , 'neg' )
    if np.minimum( np.abs(value_of_tau_neg) , np.abs(value_of_tau_pos) ) == np.abs(value_of_tau_neg):
        val_of_tau = value_of_tau_neg
    else:
        val_of_tau = value_of_tau_pos
    if np.abs( val_of_tau ) > np.pi/2:
        sys.exit('estou intersectando a crista errada')
    return val_of_tau
