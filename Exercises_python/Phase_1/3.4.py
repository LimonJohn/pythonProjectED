# 3.4 Задача «Первая цифра после точки»
from math import floor
x = float(input())
f_x = floor(x)
fractional_x = (x - f_x) * 10
print(floor(fractional_x))
