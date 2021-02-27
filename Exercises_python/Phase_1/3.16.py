# 3.16 Задача «Проценты»
P = int(input())
X = int(input())
Y = int(input())
babosiki = (X * 100 + Y) + (X * 100 + Y) * P / 100
rub = int(babosiki // 100)
kop = int(babosiki % 100)
print(rub, kop)
