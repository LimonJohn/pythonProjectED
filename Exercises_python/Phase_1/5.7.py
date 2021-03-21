# 5.7 Задача «Удаление фрагмента»
symbol = 'h'
string = input()
a, b = string.find(symbol), string.rfind(symbol)
print(string[:a] + string[b + 1:])
