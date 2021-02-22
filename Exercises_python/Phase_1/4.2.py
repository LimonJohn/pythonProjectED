# 4.2 Задача «Ряд - 2»
a = int(input())
b = int(input())
row = ()
if a < b:
    for i in range(a, b + 1):
        row = row + (i,)
else:
    for i in range(a, b - 1, -1):
        row = row + (i,)
print(row)
