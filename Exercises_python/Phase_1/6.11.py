# 6.11 Задача «Количество элементов, которые больше предыдущего»
i = int(input())
a = 0
k = 0
while i != 0:
    if i > a:
        a = i
        k += 1
    else:
        a = i
    i = int(input())
print(k - 1)
