# 5.11 Задача «Замена внутри фрагмента»
symbol = 'h'
renameTo = 'H'
string = input()
a, b = string.find(symbol), string.rfind(symbol)
stringAB = string[a + 1:b].replace(symbol, renameTo)
print(string[:a + 1] + stringAB + string[b:])
