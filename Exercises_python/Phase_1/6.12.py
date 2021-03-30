# 6.12 Задача «Второй максимум»
i = int(input())
a = 0
k = -1
while i != 0:
    if a > i > k:
        k = i
    elif i > a > k:
        k = a
        a = i
    i = int(input())
print(k)
