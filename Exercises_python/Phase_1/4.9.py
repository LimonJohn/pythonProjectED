# 4.9 Задача «Количество нулей»
s = 0
zeroes = 0
number_N = int(input())
for i in range(number_N):
    s = int(input())
    if s == 0:
        zeroes += 1
print(zeroes)
