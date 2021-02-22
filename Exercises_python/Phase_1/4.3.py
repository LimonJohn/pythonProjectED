# 4.3 Задача «Ряд - 3»
a = int(input())
b = int(input())
row = ()
a_odd = a + a % 2 - 1
for i in range(a_odd, b - 1, -2):
    row = row + (i,)
print(row)
