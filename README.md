https://schaeferrodrigo.github.io/scattering_map_project/We want to describe the scattering maps and consequently diffusion paths.

# 2 + 1/2 degree of freedom case:

In these cases the scattering map can be approximated by the level curves of the reduced Poincare function in first order.

## The simplest perturbation ![first_pert](https://latex.codecogs.com/gif.latex?%5Ccos%20q%28a_1%5Ccos%5Cvarphi%20&plus;%20a_2%5Ccos%20s%29):
**ref**: [DS2107](https://link.springer.com/article/10.1134/S1560354717010051)

### Reduced Poincaré function:
![Meln_pote_1](https://latex.codecogs.com/gif.latex?%5Cmathcal%7BL%7D%5E*%28I%2C%5Ctheta%29%20%3D%20A_1%28I%29%5Ccos%28%5Ctheta%20-%20I%5Ctau%5E*%29%20&plus;%20A_2%5Ccos%28-%5Ctau%5E*%29)

### Structure of the script:
- given I and theta, to find ![tau](https://latex.codecogs.com/gif.latex?%5Ctau%5E*)
- to apply I , theta and ![tau](https://latex.codecogs.com/gif.latex?%5Ctau%5E*) in  the reduced poincare function (to save this values in a matrix)
- to plot the level curves

### How to find ![tau](https://latex.codecogs.com/gif.latex?%5Ctau%5E*): 

We have to look for the intersecction between crests and NHIM lines.![tau](https://latex.codecogs.com/gif.latex?%5Ctau%5E*) satisfies

![eq_crest](https://latex.codecogs.com/gif.latex?%5Calpha%28I%29%5Cmu_1%20%5Csin%28%5Cvarphi%20-%20I%5Ctau%29%20&plus;%20%5Csin%28-%5Ctau%29%20%3D%200)

Steps:
- I begin with an initial value tau_0 = 0.
- to find the first tau_k = tau_0 + k* step such that (eq_crest( I , theta , tau_0 ) * eq_crest( I , theta , tau_k ) )< 0  (This is almost completely true, indeed I change tau_0 in order to obtain the next step faster).
- to apply the bissection method for these candidates.
- to apply the secant method to obtain a better solution.

### Observations:

* theta = phi - Is by definition. I can fix s = 0, so theta = phi.
* Highways are the level curves ![hig](https://latex.codecogs.com/gif.latex?%5Cmathcal%7BL%7D%5E*%20%28I%2C%5Ctheta%29%20%3D%20A_2)
 
 * Note that : ![ini_high](https://latex.codecogs.com/gif.latex?%5Cmathcal%7BL%7D%5E*%20%280%2C3%5Cpi/2%29%20%3D%20A_2)

**FILE:** [scat_map_frist_pert.zip](https://github.com/schaeferrodrigo/scattering_map_project/blob/master/scat_map_first_pert.zip) 


## Second Perturbation ![sec_pert](https://latex.codecogs.com/gif.latex?%5Ccos%20q%20%28a_1%5Ccos%5Cvarphi%20&plus;%20%5Ccos%28%5Cvarphi-s%29%29)

This case is published on [DS2107b](https://arxiv.org/pdf/1710.00029.pdf).

### Reduced Poincaré function:
![red_poin_2](https://latex.codecogs.com/gif.latex?%5Cmathcal%7BL%7D%5E*%28I%2C%5Ctheta%29%20%3D%20A_1%28I%29%5Ccos%5Cvarphi%20&plus;%20A_2%28I%29%5Ccos%28%5Csigma%20-%20%28I-1%29%5Ctau%5E*%29%2C%20%5Cquad%20%5Ctext%7Bwhere%7D%5Cquad%20%5Csigma%20%3D%20%5Cvarphi%20-s)

### Structure of the script:

 - The same for the simplest perturbation.
 
### How to find ![tau](https://latex.codecogs.com/gif.latex?%5Ctau%5E*): 

We have to look for the intersecction between crests and NHIM lines.![tau](https://latex.codecogs.com/gif.latex?%5Ctau%5E*) satisfies

![eq_crest_2](https://latex.codecogs.com/gif.latex?A_1%28I%29I%5Csin%28%5Cvarphi%20-%20I%5Ctau%29%20&plus;%20%28I-1%29A_2%28I%29%5Csin%28%5Csigma%20-%20%28I-1%29%5Ctau%29%20%3D%200)

Steps:
  - very similar.

### Observations:

* theta = phi - Is by definition. I can fix s = 0, so theta = phi.
* There is no highway.
* This code generate a special combination of scattering maps. Two straight lines in phi = pi/2 and phi = 3 * phi/2 where the scattering maps is discontinuous.

**FILE:** [scat_second_pert.zip](https://github.com/schaeferrodrigo/scattering_map_project/blob/master/scat_second_pert.zip) 

 # Caso 3 + 1/2 degree of freedom case

## The simplest perturbation ![312_first](https://latex.codecogs.com/gif.latex?a_1%20%5Ccos%5Cvarphi_1%20&plus;%20a_2%5Ccos%5Cvarphi_2%20&plus;%20a_3%5Ccos%20s):
**ref:** [Draft](https://github.com/schaeferrodrigo/scattering_map_project/blob/master/three_and_half_dof.pdf)

### Reduced Poincaré function:
![312Red_Poinc_fun](https://latex.codecogs.com/gif.latex?%5Cmathcal%7BL%7D%28I%2C%5Ctheta%29%3D%20A_1%28I_1%29%20%5Ccos%28%5Cvarphi_1%20-%20%5Comega_1%5Ctau%5E*%29%20&plus;%20A_2%28I_2%29%20%5Ccos%28%5Cvarphi_2-%5Comega_2%5Ctau%5E*%29%20&plus;%20A_3%20%5Ccos%5Ctau%5E*)

**Remark** Scattering map is not integrable

### Structure of the script:
- to apply a symplectic method to compute the scattering map:
  * To solve (by fixed point method)
  
       ![pto_fixo](https://latex.codecogs.com/gif.latex?%5Ctheta%5E%7Bk&plus;1%7D%20%3D%20%5Ctheta%5Ek%20-%20%5Cvarepsilon%20%5Cpartial_I%20%5Cmathcal%7BL%7D%28I%5Ek%20%2C%20%5Ctheta%5E%7Bk&plus;1%7D%29) 
  * and apply   
  
      ![I-k+1](https://latex.codecogs.com/gif.latex?I%5E%7Bk&plus;1%7D%20%3D%20I%5Ek%20&plus;%20%5Cvarepsilon%20%5Cpartial_%7B%5Ctheta%7D%20%5Cmathcal%7BL%7D%28I%5Ek%20%2C%20%5Ctheta%5E%7Bk&plus;1%7D%29)  
   
   
**rem:** in each step we have to computate tau^*. It is done the same method used for 2+1/2 dim. 

Since we are looking for highways, and highways are "unstable" in the 2+1/2 dof case, we apply backwards iterations of scattering map, in other words, we change -eps for eps in the above equations.


**File:** [iteracao-back.zip](https://github.com/schaeferrodrigo/scattering_map_project/blob/master/iteracao-back.zip) 

### Poincaré Section 

The Poincaré section in general I defined as theta_1 = pi.
And I look at the plot for the variables (theta_2 , I_2)

## Second Perturbation ![312_second](https://latex.codecogs.com/gif.latex?a_1%20%5Ccos%5Cvarphi_1%20&plus;%20a_2%5Ccos%5Cvarphi_2%20&plus;%20a_3%5Ccos%20%28%5Cvarphi_1%20&plus;%20%5Cvarphi_2%20-%20s%29)

[docs/README.md](https://github.com/schaeferrodrigo/scattering_map_project/blob/master/docs/README.md)

In progress


### Thecnical information

All scripts were written for python 2.7

