#-*-coding:utf8;-*-
#qpy:3
#qpy:console

from math import log as ln

h = 0.1
a = 1
b = 1.4

y = ln(h**2), ln(a**2), ln(b**2)
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print ("Спосіб №1")
print (y)


y = lambda x:ln(x**2)
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print ("Спосіб №2")
print(y(0.1))
print(y(1))
print(y(1.4))