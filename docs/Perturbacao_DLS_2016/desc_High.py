# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
import matplotlib.pyplot as plt
import sys

# coeficientes
a_1 = 0.6
a_2 = 1.
mu = a_1 / a_2

positive_I =  np.array([x for x in np.linspace(-5 , 5, 5/0.001) if x != 1 ])

def A_1(I):
    A_1 = 2* a_1 * np.pi * I/np.sinh(np.pi * I/2)
    return A_1

plt.figure()
plt.plot(positive_I , A_1(positive_I))
#plt.show()


A_2 = 2 * a_2 * np.pi/np.sinh(np.pi/2)

print A_2

def f_plus(I):
    plus = ((I**2)* A_2 + np.sqrt( (A_2)**2 + (I**2 -1)*(I**2) * A_1(I)**2 ))/((I**2 - 1)*A_2)
    return plus

def f_minus(I):
    minus = ((I**2)* A_2 - np.sqrt( (A_2)**2 + (I**2 -1)*(I**2) * A_1(I)**2 ))/((I**2 - 1)*A_2)
    return minus

plt.figure()
plt.plot( positive_I , f_plus(positive_I),'.', color= 'blue' )
plt.axis([ 0 , 5 , -1.5 , 1.5 ])

plt.figure()
plt.plot(positive_I , f_minus(positive_I), color = 'red')
plt.axis([ 0 , 5 , -1.5 , 1.5 ])

def tau_minus_1( I ):
    tau = np.arccos( f_minus( I ) )
    return tau

def tau_minus_2(I):
    tau =  -  np.arccos( f_minus( I ) )
    return tau

plt.figure()
plt.plot( positive_I , tau_minus_1(positive_I) )
plt.plot( positive_I , tau_minus_2(positive_I) )
plt.axis([ 0 , 5 , 0 , 2*np.pi ])

# def theta_minus( I ):
#     #theta = tau_plus(I)
#     theta = (-np.arcsin( ( A_2 * np.sin( tau_minus(I) ))/(I * A_1(I) ) ) - I * tau_minus(I))%(2*np.pi)
#     return theta

def theta_minus_1( I ):
    theta = (np.arccos( (A_2 *( 1 - f_minus(I)))/A_1(I)) - I * tau_minus_1(I))%(2*np.pi)
    return theta
def theta_minus_2( I ):
    theta = (- np.arccos( (A_2 *( 1 - f_minus(I)))/A_1(I)) - I * tau_minus_1(I))%(2*np.pi)
    return theta

def theta_minus_3( I ):
    theta = (np.arccos( (A_2 *( 1 - f_minus(I)))/A_1(I)) - I * tau_minus_2(I))%(2*np.pi)
    return theta
def theta_minus_4( I ):
    theta = ( - np.arccos( (A_2 *( 1 - f_minus(I)))/A_1(I)) - I * tau_minus_2(I))%(2*np.pi)
    return theta

plt.figure()
plt.plot( theta_minus_1( positive_I ) , positive_I , color = 'red')
plt.plot( theta_minus_2(positive_I) , positive_I , color= 'blue')
plt.plot( theta_minus_3( positive_I ) , positive_I , color = 'green')
plt.plot( theta_minus_4(positive_I) , positive_I , color= 'black')
plt.axis([0 , 2 * np.pi , -5, 5 ])
plt.show()

# negative_I = np.array([-x for x in np.linspace(0.00001 , 5, 5/0.001) if x != 1 ])
#
# plt.figure()
# plt.plot( theta_minus_1( negative_I ) , negative_I , color = 'red')
# plt.plot( theta_minus_2(negative_I) , negative_I , color= 'blue')
# plt.plot( theta_minus_3( negative_I ) , negative_I , color = 'green')
# plt.plot( theta_minus_4(negative_I) , negative_I , color= 'black')
# plt.axis([0 , 2 * np.pi , -5,0 ])
# plt.show()
