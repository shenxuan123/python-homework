# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:22:48 2023

@author: China
"""

w=eval(input("请输入您的体重：(kg)"))      ###体重w单位为kg
h=eval(input("请输入您的身高：(m)"))      ###身高h单位为m
t=w/(h*h)    ###体指数t
if t<18:
    print("您为低体重")
elif 18<=t and t<25:
    print("您为正常体重")
elif 25<=t and t<27:
    print("您为超重体重")
else:
    print("您为肥胖体重")
