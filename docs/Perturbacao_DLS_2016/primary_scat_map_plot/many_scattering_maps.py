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
def many_scattering_maps( domain_I_1 , domain_I_2 , domain_theta_1 , domain_theta_2 , PS ):
    "iteraçao para gerar varias órbitas de um scattering map , PS = without (default) or with Poincaré section "
    dic_I_1  , dic_I_2 , dic_theta_1 , dic_theta_2 = {}  , {} , {} , {}
    for init_I_1 in domain_I_1:
        for init_I_2 in domain_I_2:
            for init_theta_1 in domain_theta_1:
                for in_theta_2 in domain_theta_2:
                    key =  str(init_I_1)+str(init_I_2)+str(init_theta_1)+str(in_theta_2)
                    I_1_values , I_2_values , theta_1_values , theta_2_values = SM( PS , init_I_1 , init_I_2, init_theta_1 , in_theta_2)
                    dic_I_1[key] , dic_I_2[key] , dic_theta_1[key] , dic_theta_2[key] = I_1_values, I_2_values, theta_1_values , theta_2_values
    return np.array([dic_I_1 , dic_I_2 , dic_theta_1 , dic_theta_2])
