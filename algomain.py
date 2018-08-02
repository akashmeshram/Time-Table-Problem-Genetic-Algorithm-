#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sun Jul 29 11:45:09 2018

@author: akashen
"""

import random
import TimeTable
random.seed()

from gene import course
import pandas as pd
data = pd.read_csv('ter.csv')
classes = []

for i in range(data.shape[0]):
    try:
        m = int(data['slot'][i][1])
    except:
        m = 1  # data['slot'][i][0]
    for j in range(m):
        p = course(data['prof'][i], data['slot'][i], data['subno'][i],
                   m)
        classes.append(p)

#print len(classes)

TotalTT = 100
TTPopulation = []

for _ in range(TotalTT):
    p = TimeTable.TimeTable(classes.copy())
    TTPopulation.append(p)

loop = 1
while loop > 0:
    matingPool = []
    for p in range(TotalTT):
        TTPopulation[p].calcFittness()

#        print(TTPopulation[p].fitt)

        fit = 10000 // TTPopulation[p].fitt

#        print(fit)

        if fit > 200:
            for i in range(fit):
                matingPool.append(TTPopulation[p])

    size = len(matingPool)

    for p in range(TotalTT):
        a = matingPool[random.randint(0, size - 1)]
        b = matingPool[random.randint(0, size - 1)]
        TTPopulation[p] = a.crossover(b, classes)
        TTPopulation[p].mutate()

    loop -= 1


			