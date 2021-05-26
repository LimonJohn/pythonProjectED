# 7.8 Задача «Количество различных элементов»
digits = [int(digits) for digits in input().split()]
j = 1
for i in range(1, len(digits)):
    if digits[i - 1] < digits[i]:
        j += 1
print(j)
