# 4.10 Задача «Лесенка»
"""
n = int(input())
s = ()
for i in range(1, n + 1):
    s += (i,)
    print(s)
    """
n = int(input())
for i in range(1, n + 1):
    summa = 0
    for j in range(1, i + 1):
        summa += j * 10 ** (i - j)
    print(summa)
