# 7.4 Задача «Соседи одного знака»
digits = [int(digits) for digits in input().split()]
moarElem = []
for i in range(1, len(digits)):
    if digits[i - 1] * digits[i] > 0:
        moarElem.append(digits[i - 1])
        moarElem.append(digits[i])
        break
print(' '.join([str(i) for i in moarElem]))
