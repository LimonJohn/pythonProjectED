# 7.3 Задача «Больше предыдущего»
digits = [int(digits) for digits in input().split()]
moarElem = []
for i in range(1, len(digits)):
    if digits[i - 1] < digits[i]:
        moarElem.append(digits[i])
print(' '.join([str(i) for i in moarElem]))
