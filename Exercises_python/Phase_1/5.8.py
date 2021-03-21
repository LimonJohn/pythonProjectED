# 5.8 Задача «Обращение фрагмента»
symbol = 'h'
string = input()
a, b = string.find(symbol), string.rfind(symbol)
print(string[:a] + string[b:a:-1] + string[b:])
