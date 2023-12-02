# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:39:25 2023

@author: China
"""

sex=input("请输入您的性别：（F或M）")    
###F代表女性，M代表男性

faHeight=eval(input("请输入您父亲的身高：（cm）"))
moHeight=eval(input("请输入您母亲的身高：（cm）"))
###faHeight为父亲身高，moHeight为母亲身高,单位均为cm

sports=input("您是否喜爱体育锻炼：（Y/N）")
###Y表示喜爱，N表示不喜爱

diet=input("您是否有良好的饮食习惯：（Y/N）")
###Y表示良好，N表示不好

maleHeight=(faHeight+moHeight)*0.54
femaleHeight=(faHeight*0.923+moHeight)/2
###maleHeight为女性成人身高，maleHeight为男性成人身高，单位均为cm

fs=femaleHeight*1.02
fl=femaleHeight*1.015
fxl=femaleHeight*1.035
ms=maleHeight*1.02
ml=maleHeight*1.015
mxl=maleHeight*1.035


if sex=="F":
    if sports=="N" and diet=="N":
        Height=femaleHeight
        print("您的身高为：",Height,"cm")
    elif sports=="Y" and diet=="N":
        Height=fs
        print("您的身高为：",Height,"cm")
    elif sports=="N" and diet=="Y":
        Height=fl
        print("您的身高为：",Height,"cm")
    elif sports=="Y" and diet=="Y":
        Height=fxl
        print("您的身高为：",Height,"cm")
if sex=="M":
    if sports=="N" and diet=="N":
        Height=maleHeight
        print("您的身高为：",Height,"cm")
    elif sports=="Y" and diet=="N":
        Height=ms
        print("您的身高为：",Height,"cm")
    elif sports=="N" and diet=="Y":
        Height=ml
        print("您的身高为：",Height,"cm")
    elif sports=="Y" and diet=="Y":
        Height=mxl
        print("您的身高为：",Height,"cm")







