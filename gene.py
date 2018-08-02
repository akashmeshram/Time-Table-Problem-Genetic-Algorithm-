#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sun Jul 29 02:58:37 2018

@author: akashen
"""

import random
random.seed()
noOfHours = 9
noOfDays = 5


class course(object):

    def __init__(
        self,
        prof,
        year,
        sub,
        freq=1,
        ):
        self.prof = prof
        self.year = year
        self.sub = sub
        self.freq = freq
        self.slot = []
        self.lab = False
        if self.freq == 1:
            self.lab = True

    def createSlot(self):
        if not self.lab:
            self.slot = [random.randint(0, noOfDays - 1),
                         random.randint(0, noOfHours - 4)]
        else:
            self.slot = [random.randint(0, noOfDays - 1),
                         random.randint(5, noOfHours - 1)]



			