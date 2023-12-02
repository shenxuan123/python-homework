# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:55:45 2023

@author: Lenovo
"""


n=0
while n<=7:
    n+=1
    b=(n * 2)-1
    if n<=4:
        print('{0:^8}'.format(b*'*'))
    if n>4:
        c=8-n
        d=(c*2)-1
        print('{0:^8}'.format(d*'*'))
    
        













