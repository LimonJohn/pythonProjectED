# 7.10 Задача «Переставить min и max»
digits = [int(i) for i in input().split()]
maxValue = max(digits)
indexMax = digits.index(maxValue)
minValue = min(digits)
indexMin = digits.index(minValue)
digits[indexMin], digits[indexMax] = digits[indexMax], digits[indexMin]
print(' '.join([str(i) for i in digits]))
