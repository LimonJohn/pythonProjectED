# 6.2 Задача «Минимальный делитель»
number = int(input())
i = 2
while number % i != 0:
    i += 1
print(i)
