# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 21:46:47 2023

@author: China
"""


import xlrd

workbook = xlrd.open_workbook(filename=r'高新区10月20日全员核酸检测追踪情况-人员情况表.xlsx')
table = workbook.sheet_by_index(0)

table_list = table.col_values(colx=2, start_rowx=2, end_rowx=None)


table_class = workbook.sheet_by_index(1)
table_class_list = table_class.col_values(colx=2, start_rowx=1, end_rowx=None)


for class_name in table_class_list:
    if(table_list.count(class_name)):
        print(class_name)
        