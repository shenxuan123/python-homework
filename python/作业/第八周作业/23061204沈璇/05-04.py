# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 10:55:09 2023

@author: fzgc
"""
###for循环
n=int(input("请输入一个正整数n="))
s=1
for i in range(1,n+1):
    s=s*i
    i+=1
print("n！=%d"%s)




###while循环
n=int(input("请输入一个正整数n="))
i=1
s=1
while i<n:
    i+=1
    s*=i
print("n！=%d"%s)




