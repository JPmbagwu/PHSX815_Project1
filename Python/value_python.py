#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 18:43:33 2023

@author: johnpaulmbagwu
"""

import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
values = np.arange(1,7) 
prob = (0.1, 0.2, 0.3, 0.1, 0.1, 0.2) # probabilities must sum to 1
custm = stats.rv_discrete(values=(values, prob))

for i in range(10000):
    print(custm.rvs())