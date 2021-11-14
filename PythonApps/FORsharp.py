# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:33:26 2020

@author: dell
"""
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Starting date: 1 Sep 2021

N = 1000

P1 = 0
E1 = 0
I1 = 10
H1 = 0
D = 0
S2 = 0
P2 = 0
E2 = 0
I2 = 0
H2 = 0
Q = 0

S1 = N - P1 - E1 - I1 - H1 - S2 - P2 - E2 - I2 - H2 - Q

t = np.linspace(0, 300, 300)

# Parameters
# Logistic distribution

h = 0.9  # high infection ability
l = 0.01  # low infection ability 
m = 15  # The day when lockdown implemented
s = -0.5  # scale parameter

def beta2(time):
    num = h - l
    den = 1 + math.exp(-(time - m)/s)
    con = l
    return num/den + con

# Other parameters
beta11 = 0.9  # rate of I1 infecting S1
beta21 = 0.8  # rate of I2 infecting S1
beta12 = 0.7  # rate of I1 infecting S2
beta22 = 0.5  # rate of I2 infecting S2
beta32 = 0.5  # rate of Q(quarantined) infecting S2
gamma11 = 0.2  # I1 recovery rate
gamma12 = 0.1  # H1 recovery rate
gamma21 = 0.3  # I2 recovery rate
gamma22 = 0.15  # H2 recovery rate
gamma23 = 0.05  # Q(quarantined) recovery rate
v1 = 0.2  # Vax rate 1
v2 = 0.1  # Vax rate 2
omega = 0.05  # wanning rate
epsilon1 = 0.07  # incubation 1
epsilon2 = 0.05  # incubation 2
h1 = 0.2  # hospitalisation rate 1
h2 = 0.1  # hospitalisation rate 2
q = 0.1  # home quarantine rate
sigma1 = 0.5  # death rate 1
sigma2 = 0.4  # death rate 2


def model(Tup, t, N, beta11, beta21, beta12, beta22, beta32, 
          gamma11, gamma12, gamma21, gamma22, gamma23, v1, v2, omega, 
          epsilon1, epsilon2, h1, h2, q, sigma1, sigma2):
    S1, P1, E1, I1, H1, D, S2, P2, E2, I2, H2, Q = Tup
    dS1dt = -beta11 * S1 * I1 / N - beta21 * S1 * I2 / N - v1 * S1
    dP1dt = v1 * S1 + gamma11 * I1 * gamma12 * H1 - omega * P1
    dE1dt = beta11 * S1 * I1 / N + beta21 * S1 * I2 / N - epsilon1 * E1
    dI1dt = epsilon1 * E1 - gamma11 * I1 - h1 * I1
    dH1dt = h1 * I1 - gamma12 * H1 - sigma1 * H1
    dDdt = sigma1 * H1 + sigma2 * H2
    dS2dt = omega * P1 - beta12 * S2 * I1 / N - beta22 * S2 * I2 / N - beta32 * Q - v2 * S2
    dP2dt = v2 * S2 + gamma21 * I2 + gamma22 * H2 + gamma23 * Q
    dE2dt = beta12 * S2 * I1 / N + beta22 * S2 * I2 / N + beta32 * Q - epsilon2 * E2
    dI2dt = epsilon2 * E2 - gamma21 * I2 - h2 * I2 - q * I2
    dH2dt = h2 * I2 - gamma22 * H2 - sigma2 * H2
    dQdt = q * I2 - gamma23 * Q
    return dS1dt, dP1dt, dE1dt, dI1dt, dH1dt, dDdt, dS2dt, dP2dt, dE2dt, dI2dt, dH2dt, dQdt


Tup = S1, P1, E1, I1, H1, D, S2, P2, E2, I2, H2, Q
sol = odeint(model, Tup, t, args=(N, beta11, beta21, beta12, beta22, beta32, 
                                  gamma11, gamma12, gamma21, gamma22, gamma23, 
                                  v1, v2, omega, epsilon1, epsilon2, h1, h2, 
                                  q, sigma1, sigma2))
S1, P1, E1, I1, H1, D, S2, P2, E2, I2, H2, Q = sol.T

fig, ax = plt.subplots()
x1 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []
y11 = []
y12 = []
for i in range(len(t)):
    y1.append(float(S1[i]))
    y2.append(float(S2[i]))
    y3.append(float(E1[i]))
    y4.append(float(E2[i]))
    y5.append(float(H1[i]))
    y6.append(float(H2[i]))
    y7.append(float(I1[i]))
    y8.append(float(I2[i]))
    y9.append(float(P1[i]))
    y10.append(float(P2[i]))
    y11.append(float(D[i]))
    y12.append(float(Q[i]))
    x1.append(float(t[i]))
    ax.cla()
    plt.xlim((0, 300))

    ax.plot(x1, y1, label='S1')
    ax.plot(x1, y2, label='S2')
    ax.plot(x1, y3, label='E1')
    ax.plot(x1, y4, label='E2')
    ax.plot(x1, y5, label='H1')
    ax.plot(x1, y6, label='H2')
    ax.plot(x1, y7, label='I1')
    ax.plot(x1, y8, label='I2')
    ax.plot(x1, y9, label='P1')
    ax.plot(x1, y10, label='P2')
    ax.plot(x1, y11, label='D')
    ax.plot(x1, y12, label='Q')
    plt.xlabel('time / days')
    plt.ylabel('number')
    ax.legend(bbox_to_anchor=(1.005, 0), loc=3, borderaxespad=0)
    plt.pause(0.01)