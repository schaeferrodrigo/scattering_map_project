# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
from inner_vf_ode import *
#===============================================================================
def inner_dyn( iv_I_1 , iv_I_2 , iv_phi_1 , iv_phi_2 , t_max = 50000 , dt = 0.1):
    '''numerical integration of the inner dynamics '''
    orbit = np.array([])
    inner = int.ode(inner_vf_ode)
    initial_values = [ iv_I_1 , iv_I_2 , iv_phi_1 , iv_phi_2 ]
    inner.set_initial_value( initial_values )
    while inner.successful() and inner.t < t_max:
        inner.integrate( inner.t+dt )
        orbit = np.append(orbit , inner.y)
    return orbit
