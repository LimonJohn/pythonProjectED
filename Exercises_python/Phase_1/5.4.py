# 5.4 Задача «Переставить два слова»
string = input()
cutter = string.find(' ')
print(string[cutter + 1:] + ' ' + string[:cutter])
