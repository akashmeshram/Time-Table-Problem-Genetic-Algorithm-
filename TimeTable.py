#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sun Jul 29 03:20:21 2018

@author: akashen
"""

import random
random.seed()
from collections import Counter

day = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thrusday',
    4: 'Friday',
    }

noOfHours = 9
noOfDays = 5
total = noOfDays * noOfHours


class TimeTable(object):

    def __init__(self, info):
        self.info = info

        for k in self.info:
            k.createSlot()

        self.lists = [[[] for x in range(noOfHours)] for y in
                      range(noOfDays)]
        self.show = [[[] for x in range(noOfHours)] for y in
                     range(noOfDays)]
        for i in self.info:
            x = i.slot[0]
            y = i.slot[1]
            self.lists[x][y].append(i)
            self.show[x][y].append(i.sub)
        self.fittness = 1
        self.fitt = 1

    def calcFittness(self):
        for i in range(noOfDays):
            for j in range(noOfHours):
                if len(self.lists[i][j]) > 1:

#                    self.fittness += 1

                    # Hard Constraints

                    cnt = Counter()  # For Professors clash
                    cnt2 = Counter()  # For Subject clash
                    cnt3 = Counter()  # For Student year clash
                    for k in self.lists[i][j]:
                        cnt[k.prof] += 1
                        cnt2[k.sub[2]] += 1
                        cnt3[k.year] += 1

                    if cnt.most_common(1)[0][1] > 1:
                        self.fittness += 1

                    if cnt2.most_common(1)[0][1] > 1:
                        self.fittness += 1

                    if cnt3.most_common(1)[0][1] > 1:
                        self.fittness += 1

        self.fitt = self.fittness
        self.fittness = 1

    def crossover(self, other, target):
        len1 = random.randint(len(self.info) * 0.1 // 1, len(self.info)
                              * 0.9 // 1)
        newTT = TimeTable(target)
        for i in range(len(self.info)):
            if i < len1:
                newTT.info[i] = self.info[i]
            else:
                newTT.info[i] = other.info[i]
        return newTT

    def mutate(self):
        for i in range(len(self.info)):
            if not random.randint(0,1):
                self.info[i].slot = [random.randint(0, noOfDays - 1),
                        random.randint(0, noOfHours - 1)]

    def display(self):
        self.calcFittness()
        print("Fittness Value", self.fitt)
        print('Subject', 'Day', 'Hour')
        for i in self.info:
            print (i.sub, day[i.slot[0]], i.slot[1], 'hr')



			