# 3.15 Задача «Часы - 3»
from math import floor

alpha = float(input())
h = floor(alpha / 30)
m = floor(alpha % 30 * 2)
s = floor(alpha % 30 % 0.5 * 120)
print(h, m, s)
