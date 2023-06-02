#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2023/05/31 11:30:03
@Author  :   Henry Stone 
@Version :   1.0
'''

import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def main():
    y = [x*x for x in list(range(4))]
    print(y)
    x = list(range(4))
    f1 = interp1d(x,y,kind='linear')

    fig = plt.figure(num=1,figsize=(5,5))
    ax=fig.add_subplot(111)
    x = [0.5*x for x in range(7)]
    ax.plot(x, f1(x), marker = '*')
    #ax.plot(x, y, marker = 'o')
    plt.show()



if __name__ == '__main__':
    main()
