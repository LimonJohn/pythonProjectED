# 3.11 Задача «Сумма цифр»
x = int(input())
e = x % 10
d = x // 10 % 10
s = x // 100
print(e + d + s)
