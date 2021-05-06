# 7.2 Задача «Четные элементы»
digits = [int(digits) for digits in input().split() if int(digits) % 2 == 0]
# evenElem = [digits for digits in digits if digits % 2 == 0]
print(' '.join([str(i) for i in digits]))
