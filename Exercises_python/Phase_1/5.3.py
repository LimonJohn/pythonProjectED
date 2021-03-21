# 5.3 Задача «Две половинки»
string = input()
cutterBig = int(len(string) / 2 + len(string) % 2)
print(string[cutterBig:] + string[:cutterBig])
