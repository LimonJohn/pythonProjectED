# 3.10 Задача «Число десятков»
x = int(input())
if x < 10:
    print('0')
elif 10 < x < 100:
    d = x // 10
    print(d)
else:
    d = x // 10 % 10
    print(d)
