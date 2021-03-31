# 6.15 Задача «Номер числа Фибоначчи»
a = int(input())
i = 0
f_0, f_1 = 0, 1
while f_1 <= a:
    f_0, f_1 = f_1, f_0 + f_1
    i += 1
    if f_0 == a:
        print(i)
if f_0 != a:
    print(-1)
