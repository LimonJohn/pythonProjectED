# 6.9 Задача «Индекс максимума последовательности»
i = -1
a = 0
k = -1
j = 0
while i != 0:
    i = int(input())
    k += 1
    if a < i:
        a = i
        j = k
print(j)
