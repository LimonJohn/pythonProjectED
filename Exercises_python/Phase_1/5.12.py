# 5.12 Задача «Удалить каждый третий символ»
string = input()
s = ''
for i in range(len(string)):
    if i % 3 != 0:
        s += string[i]
print(s)
