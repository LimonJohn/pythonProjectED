# 7.6 Задача «Наибольший элемент»
digits = [int(digits) for digits in input().split()]
maxValue = max(digits)
index = digits.index(maxValue)
print(maxValue, index)
