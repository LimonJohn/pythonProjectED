# 4.3 Задача «Ряд - 3»
a = int(input())
b = int(input())
a_odd = a + a % 2 - 1
for i in range(a_odd, b - 1, -2):
    print(i)
