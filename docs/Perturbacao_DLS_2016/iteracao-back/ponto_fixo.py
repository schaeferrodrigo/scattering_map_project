# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
#import matplotlib.pyplot as plt
#import sys
from parametros import *
from funcoes import *
from potencial_melnikov import *
from met_tau import *
#===============================================================================
# encontrar ponto fixo
def sol_ponto_fixo( I_in_1 , I_in_2 , theta_in_1 , theta_in_2):
    "método de iteraçao simple para encontrar ponto fixo"
    tau = assign_tau( I_in_1 , I_in_2 , theta_in_1 , theta_in_2 )
    fx = np.zeros( 2 )
    fx[ 0 ] = (theta_in_1  - (-eps)* part_der_L_I_1( I_in_1 , I_in_2 , theta_in_1 , theta_in_2 , tau))%(2 * np.pi)
    fx[ 1 ] = (theta_in_2 - (-eps)* part_der_L_I_2( I_in_1 , I_in_2 , theta_in_1 , theta_in_2 , tau ))%(2 * np.pi)
    x = np.array([theta_in_1 , theta_in_2])
    passo = 0
    distancia = np.linalg.norm( (fx - x)%(2*np.pi) )
    while distancia > 1e-10:
        #print 'distancia do ponto fixo = ' , distancia
        x = fx
        tau = assign_tau( I_in_1 , I_in_2 , x[0] , x[1])
        fx[ 0 ] = ( theta_in_1  - (-eps)* part_der_L_I_1( I_in_1 , I_in_2 , x[0] , x[1] , tau))%(2 * np.pi)
        fx[ 1 ] = ( theta_in_2 - (-eps)* part_der_L_I_2( I_in_1 , I_in_2 , x[0] , x[1] , tau ))%(2 * np.pi)
        distancia = np.linalg.norm( (fx - x)%(2*np.pi) )
        passo += 1
    return np.array([x , tau])
