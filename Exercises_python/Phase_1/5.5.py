# 5.5 Задача «Первое и последнее вхождения»
symbol = 'f'
string = input()
if string.count(symbol) == 1:
    print(string.find(symbol))
elif string.count(symbol) > 1:
    print(string.find(symbol), string.rfind(symbol))
