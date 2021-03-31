# 6.16 Задача «Максимальное число идущих подряд равных элементов»
a = int(input())
i, j, b = 1, 1, 0
while a != 0:
    if a == b and j <= i:
        i += 1
        j = i
    elif a == b and j > i:
        i += 1
    else:
        i = 1
    b = a
    a = int(input())
print(j)
