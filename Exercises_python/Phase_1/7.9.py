# 7.9 Задача «Переставить соседние»
digits = [int(i) for i in input().split()]
# for i in range(len(digits)):
#     digits[i - 3], digits[i - 2] = digits[i - 2], digits[i - 3]
#     digits[i - 1], digits[i] = digits[i], digits[i - 1]
# print(' '.join([str(i) for i in digits]))
for i in range(1, len(digits), 2):
    digits[i - 1], digits[i] = digits[i], digits[i - 1]
print(' '.join([str(i) for i in digits]))
