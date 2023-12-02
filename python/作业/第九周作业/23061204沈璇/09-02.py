# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 08:50:45 2023

@author: Lenovo
"""

import time
scale = 50
print('执行开始'.center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
print("\n"+"执行结束".center(scale//2,'-'))