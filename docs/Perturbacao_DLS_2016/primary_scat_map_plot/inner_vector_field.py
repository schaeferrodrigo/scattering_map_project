# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
import parametros as par
#==============================================================================
def inner_vf_ode( t , y ):
    ''' inner vector field '''
    I_1 , I_2 , phi_1 , phi_2 , s = y
    dot_I_1 = par.eps * ( par.a_1  * np.sin( phi_1 ) + np.sin( phi_1 + phi_2 - s))
    dot_I_2 = par.eps * ( par.a_2 * np.sin( phi_2 ) + np.sin( phi_1 + phi_2 - s))
    dot_phi_1 = I_1
    dot_phi_2 = I_2
    dot_s = 1
    system = [dot_I_1 , dot_I_2 , dot_phi_1, dot_phi_2 , dot_s]
    return system
