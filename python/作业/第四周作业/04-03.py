# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:15:14 2023

@author: Lenovo
"""

has_ticket =input("请输入是否有车票（有/没有）")
knife_length =eval(input("请输入刀的长度(厘米)"))

if has_ticket=="有":
    print("需要进行安检")
    if knife_length>20:
        print("刀已超过20厘米，不允许上车")
    else:
        print("安检通过")
else:
    print("不允许通过，请补票")