import numpy as np

def f(x):
    return (x-1)*(x-1)-1

def dichotomie(f,a,b,eps=1e-8):
    c=(a+b)/2
    fa=f(a)
    fc=f(c)







    return c

a=1.0
b=10.0
for eps in np.logspace(0,-12,13):
    print("eps={:e},x*={:1.16f}".format(eps,dichotomie(f,a,b,eps)))