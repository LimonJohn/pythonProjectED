# 6.8 Задача «Максимум последовательности»
i = -1
a = 0
while i != 0:
    i = int(input())
    if a < i:
        a = i
print(a)
