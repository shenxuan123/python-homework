# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:15:43 2023

@author: Lenovo
"""

import random as b
a = eval(input("请输入一个数字"))
c = b.randint(1,3)
#####1代表石头，2代表剪刀，3代表布
if a==1 and c==2:
    print("人赢")
elif a==2 and c==3:
    print("人赢")
elif a==3 and c==1:
    print("人赢")
else:
    print("电脑赢")
    








