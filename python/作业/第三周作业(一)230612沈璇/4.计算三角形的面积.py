# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:25:42 2023

@author: China
"""

a = float(input ("请输入一个数字："))
b = float(input ("请输入一个数字："))
c = float(input ("请输入一个数字："))
if ( a + b > c and a - b < c and a > 0 and b > 0 and c > 0):
    p = 0.5 * (a + b + c)
    S = pow(p * (p - a) * (p - b) * (p - c), 0.5)
    print (S)
else:
    print ("false")
