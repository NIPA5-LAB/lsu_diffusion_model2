#!/usr/bin/env python
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def plot_profile(x,y, color="r", title=None):
    plt.figure()
    plt.plot(x, y, color)
    plt.xlabel("X")
    plt.ylabel("C")
    plt.title(title)
    
D = 100
Lx = 300
dx = 0.5 #grid spacing
x = np.arange (start=0, stop=Lx, step=dx) #arrange function
nx = len(x) #how many  bujhay len function 

C = np.zeros_like(x)
C_left = 500
C_right = 0
C[x <= Lx//2] =C_left #c for values of x that are less than half the domain size are set to be on left, // is important
C[x > Lx//2] =C_right

plot_profile(x,C)
plt.savefig("initial_profile.png")

nt = 5000
dt = 0.5 * dx**2/D

for t in range (0, nt):
    C[1:-1]+= D * dt/ dx ** 2* (C[:-2] -2*C[1:-1] + C[2:])# dt is time step and dx is grid spacing, C is for concentration, 

plot_profile(x,C, color="b", title="blah")
plt.savefig("final_profile.png")





