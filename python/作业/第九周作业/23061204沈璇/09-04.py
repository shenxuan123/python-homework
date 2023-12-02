# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:05:11 2023

@author: Lenovo
"""
num=[]
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            num.append(i)
print('100以内的质数：%s'%num)









