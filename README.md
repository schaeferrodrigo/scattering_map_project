<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

We want to describe the scattering maps and consequently diffusion paths.

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

*FILE:* [scat_map_frist_pert.zip](https://github.com/schaeferrodrigo/scattering_map_project/blob/master/scat_map_first_pert.zip) 






## Second Perturbation

This case is published on [DS2107b](https://arxiv.org/pdf/1710.00029.pdf)


# Caso 3 + 1/2 degree of freedom case

## The simplest perturbation

## Second Perturbation







### Thecnical information

All scripts were written for python 2.7

## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/schaeferrodrigo/scattering_map_project/edit/master/README.md) to maintain and preview the content for your website in Markdown files. teste

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/schaeferrodrigo/scattering_map_project/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.



Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
