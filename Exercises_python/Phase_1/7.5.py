# 7.5 Задача «Больше своих соседей»
digits = [int(digits) for digits in input().split()]
j = 0
for i in range(1, len(digits) - 1):
    if digits[i - 1] < digits[i] > digits[i + 1]:
        j += 1
print(j)
