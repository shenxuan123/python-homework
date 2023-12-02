# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 09:05:01 2023

@author: Lenovo
"""
import random as a
c=a.randint(0,101)
n=1
while n<101:
    b=eval(input("请输入一个数字："))
    if b<c:
        print('小了')
    if b>c:
        print('大了')
    if b==c:
        print(n)
        break
    n+=1































