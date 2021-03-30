# 6.13 Задача «Количество элементов, равных максимуму»
i = int(input())
max_el = 0
amount = 1
while i != 0:
    if i > max_el:
        max_el = i
        amount = 1
    elif i == max_el:
        amount += 1
    i = int(input())
print(amount)
