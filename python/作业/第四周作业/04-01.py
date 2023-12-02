# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:14:00 2023

@author: Lenovo
"""

age = int(input("请输入正常人的年龄"))
if age > 0 and age <= 120:
    print("true")
else:
    print("false")
    
###
python_score = eval(input("请输入成绩"))
c_score = eval(input("请输入成绩"))
if python_score > 60 or c_score > 60:
    print("合格")
else:
    print("不合格")
    
###

is_employee = input("请输入是否为本公司员工（是/否）")
if  is_employee=="是":
    print("欢迎光临")
else:
    print("您不是本公司的员工，不允许入内")