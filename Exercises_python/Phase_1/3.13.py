# 3.13 Задача «Часы - 1»
H = int(input())
M = int(input())
S = int(input())
alpha = H * 30 + M * 30 / 60 + S * 30 / 3600
print(alpha)
