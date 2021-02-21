# 3.9 Задача «Улитка»
from math import ceil

h = int(input())
a = int(input())
b = int(input())
if h <= a:
    print('1')
else:
    days = (h - b) / (a - b)
    print(ceil(days))
