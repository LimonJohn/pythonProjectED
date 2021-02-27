# 2.3 Шахматная доска
a = []
for i in range(4):
    a.append(int(input()))
if a[0] % 2 == 0 and a[1] % 2 == 0 or a[0] % 2 != 0 and a[1] % 2 != 0:
    b = 0
else:
    b = 1
if a[2] % 2 == 0 and a[3] % 2 == 0 or a[2] % 2 != 0 and a[3] % 2 != 0:
    c = 0
else:
    c = 1
if b == c:
    print('YES')
else:
    print('NO')
