# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:33:26 2020

@author: dell
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N = input('Total population')
I = input('Infected people')
N = int(N)
I = int(I)
E = 0
R = 0
D = 0
beta = 1.5  # infection ability
gamma = 0.1  # recovery
delta = 0.2  # incubation days
alpha = 0.2  # death rate
rho = 0.1  # time till death
S = N - I - R - D -E
t = np.linspace(0, 100, 100)


def model(Tup, t, N, beta, gamma, delta, alpha, rho):
    S, E, I, R, D = Tup
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - E * delta
    dIdt = delta * E - (1 - alpha) * gamma * I - alpha * rho * I
    dRdt = (1 - alpha) * gamma * I
    dDdt = alpha * rho * I
    return dSdt, dEdt, dIdt, dRdt, dDdt


Tup = S, E, I, R, D
sol = odeint(model, Tup, t, args=(N, beta, gamma, delta, alpha, rho))
S, E, I, R, D = sol.T

fig, ax = plt.subplots()
x1 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
for i in range(len(t)):
    y1.append(float(S[i]))
    y2.append(float(E[i]))
    y3.append(float(I[i]))
    y4.append(float(R[i]))
    y5.append(float(D[i]))
    x1.append(float(t[i]))
    ax.cla()
    plt.xlim((0, 100))
    my_x_ticks = np.arange(0, 100, 10)

    ax.plot(x1, y1, label='Susceptible')
    ax.plot(x1, y2, label='Exposed')
    ax.plot(x1, y3, label='Infected')
    ax.plot(x1, y4, label='Recovered')
    ax.plot(x1, y5, label='Dead')
    plt.xlabel('time / days')
    plt.ylabel('number')
    ax.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
    plt.pause(0.1)
