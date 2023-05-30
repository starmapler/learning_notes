#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   plot.py
@Time    :   2023/05/24 15:17:43
@Author  :   Henry Stone 
@Version :   1.0
'''

import matplotlib.pyplot as plt
import numpy as np
from random import randint
import matplotlib.colors as mcolors
import pandas as pd
import xlrd
import glob
import sys
import argparse

def main():
    draw()

def draw():
    xzhou = [1.0 1.1 1.2 1.3 1.4 1.5 1.55 1.6 1.65 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4]
    yzhou = [0.203	0.257	0.333	0.450	0.711	1.050	1.530	1.595	1.471	1.167	0.745	0.547	0.437	0.352	0.302	0.264	0.235]
    j = 0
    fig = plt.figure(num=1,figsize=(5,5))
    ax=fig.add_subplot(111)

    #names = glob.glob(filename + '*')
    i = 0
    
    colors=list(mcolors.CSS4_COLORS.keys())
    ax.plot(xzhou, yzhou, 
            color = mcolors.CSS4_COLORS[colors[i+3]],
            label = '$ 100 \Omega $', marker = 'o')
    i = i + 1
    
    #plt.xlim(0, 105)
    #plt.ylim(0.2e-7, 1.8e-7)
    #plt.rc('font', size=16)
    ax.yaxis.get_offset_text().set_fontsize(18)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), labelsize=18)
    plt.tick_params(labelsize = 18) #坐标轴刻度字体大小设置
    plt.legend(ncol = 2,  
               prop={ 'size' : 18})
    plt.xlabel('Voltage [V]', loc = 'right', 
               fontdict={'family' : 'Times New Roman', 'size' : 22})
    plt.ylabel('$ C^{-2} [pF^{-2}] $', loc = 'top', 
               fontdict={'family' : 'Times New Roman', 'size' : 22})
    plt.show()
    
    

def iv(filename):
    voltage = []
    current = []

    fig = plt.figure(num=1,figsize=(5,5))
    ax=fig.add_subplot(111)

    names = glob.glob(filename + '*')
    i = 0
    for name in names:

        voltage = []
        current = []
        with open(name, 'r') as f:
            print(1)
            for line in f.readlines():                
                try:
                    fargs = list(map(float, line.strip('\n').strip().split(',')))
                    voltage.append(-fargs[0])
                    current.append(fargs[4] * 1e9)
                except Exception as e:
                    print(str(e))
                    pass
        voltage.pop(0)
        current.pop(0)
        #print(voltage)
        #print(current)
        """
        worksheet = xlrd.open_workbook('I_V(1).xls')
        sheet_names= worksheet.sheet_names()

        for sheet_name in sheet_names:
            sheet = worksheet.sheet_by_name(sheet_name)
            rows = sheet.nrows # 获取行数
            cols = sheet.ncols # 获取列数，尽管没用到
            all_content = []
            all_v = []

            for j in range(rows) :
                cell = sheet.cell_value(j, i-1) # 取第二列数据
                v = sheet.cell_value(j, 0)
                try:
                    cell = float(cell) # 转换为浮点数
                    v = float(v)
                    all_content.append(cell)
                    all_v.append(v)
                except ValueError:
                    pass
        #print(all_v)"""
        colors=list(mcolors.CSS4_COLORS.keys())
        #print(colors)
        ax.plot(voltage, current, 
                color = mcolors.CSS4_COLORS[colors[i+3]], 
                label = name + ' IHEP', 
                marker = 'o')
        """
        ax.plot(all_v, all_content, 
                color = mcolors.CSS4_COLORS[colors[i+3]], 
                label = name + ' HPK', 
                marker = '^')
        """
        i = i + 1
    plt.rc('font', size=16)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8 , box.height])
    ax.legend(loc='center right', bbox_to_anchor=(1.42, 0.5), ncol=2)

    #plt.ylim(0, 200)

    #ax.yaxis.get_offset_text().set_fontsize(16)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), labelsize=18)
    plt.tick_params(labelsize = 18) #坐标轴刻度字体大小设置
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0), labelsize=18)
    #plt.legend(ncol = 2)

    plt.xlabel('Voltage [V]', loc = 'right', 
               fontdict={'family' : 'Times New Roman', 'size' : 22})
    plt.ylabel('Current [nA]', loc = 'top', 
               fontdict={'family' : 'Times New Roman', 'size' : 22})
    plt.show()

def oiv(voltage, current, n):
    worksheet = xlrd.open_workbook('I_V(1).xls')
    sheet_names= worksheet.sheet_names()
    print(sheet_names)
    for sheet_name in sheet_names:
        sheet = worksheet.sheet_by_name(sheet_name)
        rows = sheet.nrows # 获取行数
        cols = sheet.ncols # 获取列数，尽管没用到
        all_content = []
        all_v = []

        for i in range(rows) :
            cell = sheet.cell_value(i, n-1) # 取第二列数据
            v = sheet.cell_value(i, 0)
            try:
                cell = float(cell) # 转换为浮点数
                v = float(v)
                all_content.append(cell)
                all_v.append(v)
            except ValueError:
                pass
        current = all_content
        voltage = all_v
        print(current)
        print(voltage)

if __name__ == '__main__':
    main()

