# 6.10 Задача «Количество четных элементов последовательности»
i = int(input())
even_n = 0
while i != 0:
    if i % 2 == 0:
        even_n += 1
    i = int(input())
print(even_n)
