# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:53:51 2020

@author: dell
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()

Snum = 1000  # int(input('Susceptible?'))
Inum = 10  # int(input('Infected?'))
Days = 100  # int(input('Days?'))
# Other parameters
MovSpe = 0.8  # The lower, the faster
InfDis = 5  # Infection Distance
InfRat = 0.05
RecRat = 0.3
NDP1 = 30  # Normal Distribution Paras
NDP2 = 10


def distance(x1, y1, x2, y2):
    return math.sqrt((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2)


data_y = list(100 * np.random.random(Snum))
data_x = list(100 * np.random.random(Snum))
data_y2 = list(100 * np.random.random(Inum))
data_x2 = list(100 * np.random.random(Inum))
data_x3 = []
data_y3 = []
recday = []
infday = []
t = []
grax = []
grax2 = []
grax3 = []


def move():
    length = len(data_y)
    length2 = len(data_y2)
    length3 = len(data_y3)
    for a in range(length):
        data_y[a] = data_y[a] + (2 * random.random() - 1) / MovSpe
        data_x[a] = data_x[a] + (2 * random.random() - 1) / MovSpe
    for b in range(length2):
        data_y2[b] = data_y2[b] + (2 * random.random() - 1) / MovSpe
        data_x2[b] = data_x2[b] + (2 * random.random() - 1) / MovSpe
    for c in range(length3):
        data_y3[c] = data_y3[c] + (2 * random.random() - 1) / MovSpe
        data_x3[c] = data_x3[c] + (2 * random.random() - 1) / MovSpe
    return data_x, data_x2, data_y, data_y2


def recover():
    for u, v, w, x in zip(data_x2, data_y2, infday, recday):
        if random.random() < RecRat and w > x:
            data_x3.append(u)
            data_y3.append(v)
            data_x2.remove(u)
            data_y2.remove(v)
    return data_x2, data_y2, data_x3, data_y3


for i in range(Days):
    recover()
    move()
    for j, n in zip(data_x, data_y):
        for k, m in zip(data_x2, data_y2):
            if distance(j, n, k, m) < InfDis and random.random() < InfRat:
                data_x2.append(j)
                data_y2.append(n)
                recday.append(random.normalvariate(NDP1, NDP2))
                infday.append(0)
                data_x.remove(j)
                data_y.remove(n)
                break
    plt.figure(1)
    ax.cla()
    plt.axis('off')
    plt.xlim((0, 100))
    plt.ylim((0, 100))
    my_x_ticks = np.arange(0, 100, 10)
    my_y_ticks = np.arange(0, 100, 10)
    ax.scatter(data_x, data_y, 5)
    ax.scatter(data_x2, data_y2, 5)
    ax.scatter(data_x3, data_y3, 5)
    for d in range(len(infday)):
        infday[d] = infday[d] + 1
    plt.pause(0.01)
    grax.append(len(data_x))
    grax2.append(len(data_x2))
    grax3.append(len(data_x3))
    t.append(len(grax))
    plt.figure(2)
    plt.clf()
    plt.xlim((0, Days))
    plt.ylim((0, Snum + Inum))
    plt.plot(t, grax)
    plt.plot(t, grax2)
    plt.plot(t, grax3)
    plt.pause(0.01)
