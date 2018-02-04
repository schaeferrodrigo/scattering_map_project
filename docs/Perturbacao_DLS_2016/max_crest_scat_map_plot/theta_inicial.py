# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
import matplotlib.pyplot as plt
import sys
from parametros import *
from funcoes import *
from potencial_melnikov import *
from met_tau import *
from ponto_fixo import *
#===============================================================================
def Valor_initial( I_1, I_2 , theta_1 ,theta_2 ):
    tau_associado = assign_tau( I_1 , I_2, theta_1 , theta_2 )
    F = L(I_1 , I_2, theta_1 , theta_2 , tau_associado ) 
    return F

def bissec( I_1, I_2 ,theta_1,  theta_2 , cand  , tol = 1e-2):
    while np.abs(theta_1 - cand)> tol:
        theta_med = (theta_1 + cand)/2
        if Valor_initial( I_1 , I_2, theta_1, theta_2) * Valor_initial(I_1, I_2, theta_med , theta_2 )< 0:
            cand = theta_med
        else:
            theta_1 = theta_med
    return [theta_1 , cand]

def secante( I_1 , I_2 , theta_2 , candidatos , tol = 1e-6):
    cand_1 , cand_2 = candidatos
    func_cand_1 , fun_cand_2 = Valor_initial(I_1, I_2, cand_1 , theta_2) , Valor_initial(I_1, I_2, cand_2 , theta_2)
    theta_sec = cand_1 - func_cand_1 * (cand_1 - cand_2)/(func_cand_1 - fun_cand_2)
    fun_sec = Valor_initial(I_1, I_2, theta_sec, theta_2)
    while np.abs(fun_sec) < tol:
        if func_cand_1 * fun_sec < 0:
            cand_2 = theta_sec
        else:
            cand_1 = theta_sec
        theta_sec = cand_1 - func_cand_1 * (cand_1 - cand_2)/(func_cand_1 - fun_cand_2)
        fun_sec = Valor_initial(I_1, I_2, theta_sec, theta_2)
    return theta_sec

def sol_theta_initial( I_1 , I_2 , theta_1, theta_2 ,tol = 1e-3):
    fun_initial = Valor_initial( I_1, I_2, theta_1 , theta_2 )
    print fun_initial
    if np.abs( fun_initial ) < tol:
        theta_final = theta_1
    else:
        step = 0.1
        theta_pos , theta_neg = theta_1 + step , theta_1 - step
        fun_pos , fun_neg = Valor_initial( I_1, I_2, theta_pos , theta_2 ) , Valor_initial( I_1, I_2, theta_neg , theta_2 )
        #passo =
        while fun_neg * fun_initial > 0 and fun_pos * fun_initial > 0 :
            print fun_neg * fun_initial , fun_pos * fun_initial
            theta_pos , theta_neg = theta_pos + step , theta_neg - step
            fun_pos , fun_neg = Valor_initial( I_1, I_2, theta_pos , theta_2 ) , Valor_initial( I_1, I_2, theta_neg , theta_2 )
        if  fun_neg * fun_initial < 0:
            cand = theta_neg
        else:
            cand = theta_pos
        candidatos = bissec(I_1, I_2 , theta_1, theta_2 , cand)
        theta_final = secante(I_1, I_2, theta_1 , candidatos )
    return theta_final
