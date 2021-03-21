# 5.6 Задача «Второе вхождение»
symbol = 'f'
string = input()
if string.count(symbol) == 0:
    print(-2)
elif string.count(symbol) == 1:
    print(-1)
elif string.count(symbol) > 1:
    print(string.find(symbol, 1 + string.find(symbol)))
