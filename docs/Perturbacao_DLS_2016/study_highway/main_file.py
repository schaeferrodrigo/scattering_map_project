# -*- coding: utf-8 -*-
#===============================================================================
# Objetivo: verificar se as highways de 3+1/2 dof tem a mesma expressao
#===============================================================================
import numpy as np
from def_theta import *
from dot_I import *
from RPF_and_crista import *
from func_coeficientes import *
from find_tau import *
from parametros import *
import matplotlib.pyplot as plt
from scat_cand import *
#===============================================================================
I_1 , I_2 = 0.001 , 0.001 # valores iniciais de I
theta_1,theta_2 = theta_H_1( I_1 ) , theta_H_2( I_2 ) #valores iniciais de theta
tau = assign_tau(I_1, I_2, theta_1 , theta_2) #tau estrela inicial

#scattering map and candidates
scat_map , cand = {} , {}
#conjunto de valores das variáveis I and theta

scat_map['I_1'] , scat_map['I_2']  = np.array([I_1]) , np.array([I_2])
scat_map['theta_1'],scat_map['theta_2']= np.array([ theta_1]),np.array([theta_2])

cand['I_1'] , cand['I_2']  = np.array([I_1]) , np.array([I_2])
cand['theta_1'], cand['theta_2']= np.array([ theta_1]),np.array([theta_2])

#Controle de que os pontos gerados de fato sao pontos de iteraçao do scattering
# map. "controle_1" controle da energia , "controle_2" satisfaz a equaçao da
# crista. "tol_1" tolerancia de erro do "controle_1" , "tol_2" tolerancia de
# erro do "controle_2"
RPF = Red_Poinc_function( I_1 , I_2 , theta_1 , theta_2, tau)
crista = eq_crest( I_1, I_2, theta_1, theta_2 , tau)
controle_1 ,controle_2 = np.abs( RPF - A_3) , np.abs(crista)
tol_1 = 1e-4
tol_2 = tol_1

#conjunto de valores dos controles
control_1 , control_2 = {} , {}
control_1['cand'] , control_1['scat'] =  np.array([ controle_1 ] ) , np.array([ controle_1 ] )
control_2['cand'] , control_2['scat'] =  np.array([ controle_2 ] ) , np.array([ controle_2 ] )


# Controle de numero de iteraçoes do scattering map
n_iter , n_max = 0 , 100000

s_I_1 , s_I_2 , s_theta_1 , s_theta_2 = I_1 , I_2, theta_1 , theta_2
c_I_1 , c_I_2 , c_theta_1 , c_theta_2 = I_1 , I_2, theta_1 , theta_2
s_tau , c_tau = tau , tau
#Iteraçao do scattering map
while  n_iter < n_max:
    #candidatos
    c_I_1 , c_I_2 , c_theta_1 , c_theta_2 = candidates( c_I_1 , c_I_2, c_tau)
    c_tau = assign_tau( c_I_1, c_I_2, c_theta_1 , c_theta_2 )
    c_RPF = Red_Poinc_function( c_I_1 , c_I_2 , c_theta_1 , c_theta_2, c_tau)
    c_crista = eq_crest( c_I_1, c_I_2, c_theta_1, c_theta_2 , c_tau)
    c_controle_1 ,c_controle_2 = np.abs( c_RPF - A_3) , np.abs(c_crista)
    cand['I_1'] , cand['I_2'] = np.append( cand['I_1'] , [ c_I_1 ]),np.append( cand['I_2'] , [ c_I_2 ])
    cand['theta_1'] , cand['theta_2'] = np.append( cand['theta_1'] , [ c_theta_1 ] ) , np.append( cand['theta_2'] , [ c_theta_2 ] )
    control_1['cand'] = np.append( control_1['cand'] , [c_controle_1])
    control_2['cand'] = np.append( control_2['cand'] , [c_controle_2])
    #scattering map
    s_I_1 , s_I_2 , s_theta_1 , s_theta_2 = scattering( s_I_1 , s_I_2, s_theta_1, s_theta_2 , s_tau)
    s_tau = assign_tau( s_I_1, s_I_2, s_theta_1 , s_theta_2 )
    s_RPF = Red_Poinc_function( s_I_1 , s_I_2 , s_theta_1 , s_theta_2, s_tau)
    s_crista = eq_crest( s_I_1, s_I_2, s_theta_1, s_theta_2 , s_tau)
    s_controle_1 ,s_controle_2 = np.abs( s_RPF - A_3) , np.abs(s_crista)
    scat_map['I_1'] , scat_map['I_2'] = np.append( scat_map['I_1'] , [ s_I_1 ]),np.append( scat_map['I_2'] , [ s_I_2 ])
    scat_map['theta_1'] , scat_map['theta_2'] = np.append( scat_map['theta_1'] , [ s_theta_1 ] ) , np.append( scat_map['theta_2'] , [ s_theta_2 ] )
    control_1['scat'] = np.append( control_1['scat'] , [s_controle_1])
    control_2['scat'] = np.append( control_2['scat'] , [s_controle_2])
    #
    n_iter += 1
    print n_iter
#iteraçao back
back_sc = {}
back_sc['I_1'] , back_sc['I_2'] = np.array([c_I_1]) , np.array([c_I_1])
back_sc['theta_1'] , back_sc['theta_2'] = np.array([c_theta_1]) , np.array([ c_theta_2])
control_1['back'] , control_2['back'] = np.array( [c_controle_1]) , np.array([c_controle_2])
max_steps = n_iter
b_I_1 , b_I_2 , b_theta_1 , b_theta_2 = c_I_1, c_I_2 , 3*np.pi/2 , 3*np.pi/2
b_tau = c_tau
while n_iter > 0:
    b_I_1 , b_I_2 , b_theta_1, b_theta_2 = back_scat( b_I_1, b_I_1 , b_theta_1 , b_theta_2 , b_tau)
    b_tau = assign_tau( b_I_1, b_I_2, b_theta_1 , b_theta_2 )
    b_RPF = Red_Poinc_function( b_I_1 , b_I_2 , b_theta_1 , b_theta_2, b_tau)
    b_crista = eq_crest( b_I_1, b_I_2, b_theta_1, b_theta_2 , b_tau)
    b_controle_1 ,b_controle_2 = np.abs( b_RPF - A_3) , np.abs(b_crista)
    back_sc['I_1'] , back_sc['I_2'] = np.append( back_sc['I_1'] , [ b_I_1 ]),np.append( back_sc['I_2'] , [ b_I_2 ])
    back_sc['theta_1'] , back_sc['theta_2'] = np.append( back_sc['theta_1'] , [ b_theta_1 ] ) , np.append( back_sc['theta_2'] , [ b_theta_2 ] )
    control_1['back'] = np.append( control_1['back'] , [b_controle_1])
    control_2['back'] = np.append( control_2['back'] , [b_controle_2])
    n_iter -=1
    print n_iter

# back_sc['I_1'] , back_sc['I_2'] , back_sc['theta_1'] , back_sc['theta_2'] = SM( c_theta_2 , 0 , c_I_1 , c_I_2)
#

control_1['back'] , control_2['back']= control_1['back'][::-1] ,control_2['back'][::-1]
# val_I_1 = open( "value_I_1.txt" , "w"  )
# val_I_1.write(values_I_1)
# val_I_1.close()
# val_I_1 = open("value_I_1.txt", "r")
# print val_I_1.read()
plt.figure()
plt.title(r'$a_1 = 0.3 $')
plt.xlabel(r'$\theta_1$' , fontsize = 25)
plt.ylabel('$I_1$' , fontsize = 25 , rotation = 'horizontal')
plt.axis([0 , 2 * np.pi , 0 , 5 ])
plt.plot( cand['theta_1'] , cand['I_1'] , color = 'blue')
plt.plot( scat_map['theta_1'] , scat_map['I_1'] , color = 'red')
plt.plot( back_sc['theta_1'] , back_sc['I_1'] , color = 'green')
plt.figure()
plt.title(r'$a_2 = 0.3 $')
plt.xlabel(r'$\theta_2$' , fontsize = 25)
plt.ylabel('$I_2$' , fontsize = 25 , rotation = 'horizontal')
plt.axis([0 , 2 * np.pi , 0 , 5 ])
plt.plot( cand['theta_2'] , cand['I_2'] , color = 'blue')
plt.plot( scat_map['theta_2'] , scat_map['I_2'] , color = 'red')
plt.plot( back_sc['theta_2'] , back_sc['I_2'] , color = 'green')
plt.figure()
plt.plot( control_1['cand'] )
plt.plot( control_1['scat'] , color = 'red' )
plt.plot(control_1['back'] , color = 'green')
plt.xlabel("nombre d'iterades" , fontsize = 15)
plt.ylabel(r'$erro_1$' , fontsize = 25 )
plt.title(r'$erro_1 = \left|\mathcal{L}^*(I,\theta_H) - A_3\right|$')
plt.figure()
plt.plot( control_2['cand'] )
plt.plot( control_2['scat'] ,color = 'red' )
plt.plot(control_2['back'] ,color = 'green')
plt.xlabel("nombre d'iterades" , fontsize = 15)
plt.ylabel(r'$erro_2$' , fontsize = 25 )
plt.title(r'$erro_2 = $equaccio de la crista')


dif_theta_1 = scat_map['theta_1'] - cand['theta_1']
dif_theta_2 = scat_map['theta_2'] - cand['theta_2']
dif_I_1 = scat_map['I_1'] - cand['I_1']
dif_I_2 = scat_map['I_2'] - cand['I_2']
b_dif_theta_1 = back_sc['theta_1'] - cand['theta_1']
b_dif_theta_2 = back_sc['theta_2'] - cand['theta_2']
b_dif_I_1 = back_sc['I_1'] - cand['I_1']
b_dif_I_2 = back_sc['I_2'] - cand['I_2']
plt.figure()
plt.plot( dif_theta_1 , 'red' )
plt.plot( b_dif_theta_1 , 'green' )
plt.title('difference between theta_1')
plt.figure()
plt.plot( dif_theta_2 , 'red' )
plt.plot( b_dif_theta_2 , 'green' )
plt.title('difference between theta_2')
plt.figure()
plt.plot( dif_I_1 ,'red')
plt.plot( b_dif_I_1  , 'green')
plt.title('difference between I_1')
plt.figure()
plt.plot( dif_I_2, 'red')
plt.plot( b_dif_I_2, 'green')
plt.title('difference between I_2')
plt.show()
