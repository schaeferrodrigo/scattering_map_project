# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
#import matplotlib.pyplot as plt
#import sys
from parametros import *
from funcoes import *
from potencial_melnikov import *
from met_tau import *
from ponto_fixo import *
from scattering_map_function import *
#===============================================================================
def many_scattering_maps( domain_theta_2  ):
    "iteraçao para gerar varias órbitas de um scattering map"
    dic_I_1  , dic_I_2 , dic_theta_1 , dic_theta_2 = {}  , {} , {} , {}
    for in_theta_2 in domain_theta_2:
        key =  str(in_theta_2)
        I_1_values , I_2_values , theta_1_values , theta_2_values = SM( in_theta_2 )
        dic_I_1[key] , dic_I_2[key] , dic_theta_1[key] , dic_theta_2[key] = I_1_values, I_2_values, theta_1_values , theta_2_values
    return np.array([dic_I_1 , dic_I_2 , dic_theta_1 , dic_theta_2])
