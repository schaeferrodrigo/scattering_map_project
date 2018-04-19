# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from dot_I import *
from def_theta import *
from parametros import *
from find_tau import *
#===============================================================================

def candidates( I_1 , I_2, tau):
    J_1 = I_1  + eps * dot_I_1( I_1, theta_H_1( I_1 ) , tau )
    J_2 = I_2 + eps * dot_I_2( I_2 , theta_H_2( I_2 ) , tau )
    phi_1 , phi_2 = theta_H_1( I_1 ) , theta_H_2( I_2 )
    return [J_1 , J_2 , phi_1 , phi_2]

def scattering( I_1 , I_2 , theta_1, theta_2, tau):
    J_1 = I_1  + eps * dot_I_1( I_1,  theta_1 , tau )
    J_2 = I_2 + eps * dot_I_2( I_2 , theta_2 , tau )
    phi_1 = theta_1  + eps * dot_theta_1( I_1 , theta_1 , tau)
    phi_2 = theta_2 + eps * dot_theta_2( I_2, theta_2 , tau )
    return [J_1 , J_2 , phi_1 , phi_2]


def sol_ponto_fixo( I_in_1 , I_in_2 , theta_in_1 , theta_in_2):
    "método de iteraçao simple para encontrar ponto fixo"
    tau = assign_tau( I_in_1 , I_in_2 , theta_in_1 , theta_in_2 )
    fx = np.zeros( 2 )
    fx[ 0 ] = (theta_in_1  + (-eps)* dot_theta_1( I_in_1 , theta_in_1  , tau))%(2 * np.pi)
    fx[ 1 ] = (theta_in_2 + (-eps)* dot_theta_2(  I_in_2  , theta_in_2 , tau ))%(2 * np.pi)
    x = np.array([theta_in_1 , theta_in_2])
    passo = 0
    distancia = np.linalg.norm( (fx - x)%(2*np.pi) )
    while distancia > 1e-10:
        #print 'distancia do ponto fixo = ' , distancia
        x = fx
        tau = assign_tau( I_in_1 , I_in_2 , x[0] , x[1])
        fx[ 0 ] = ( theta_in_1  + (-eps)* dot_theta_1( I_in_1 , x[0] , tau))%(2 * np.pi)
        fx[ 1 ] = ( theta_in_2 + (-eps)* dot_theta_2( I_in_2 , x[1] , tau ))%(2 * np.pi)
        distancia = np.linalg.norm( (fx - x)%(2*np.pi) )
        passo += 1
    return np.array([x , tau])

def back_scat( I_1 , I_2 , theta_1 , theta_2 , tau):
    theta , tau_int = sol_ponto_fixo( I_1, I_2 , theta_1 ,theta_2)
    J_1 = I_1 + (-eps) * dot_I_1( I_1 , theta[0] , tau_int )
    J_2 = I_2 + (-eps) * dot_I_2( I_2,  theta[1] , tau_int )
    return [J_1, J_2 , theta[0] , theta[1]]
