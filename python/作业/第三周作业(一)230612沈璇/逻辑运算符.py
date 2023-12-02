# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:58:02 2023

@author: Lenovo
"""

a = 10
b = 20

if ( a and b ):
    print ("1 - 变量 a 和 b 都为 true")
else:
    print ("1 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
    print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print ("2 - 变量 a 和 b 都不为 true")
    
#修改变量里 a 的值
a = 0
if ( a and b ):
    print ("3 - 变量 a 和 b 都为 true")
else:
    print ("3 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
    print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print ("4 - 变量 a 和 b 都不为 true")

if ( a and b ):
    print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print ("5 - 变量 a 和 b 都为 true")





