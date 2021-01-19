# 2.12 Шоколадка
s = []
for i in range(3):
    s.append(int((input())))
if s[2] < s[0] * s[1] and (s[2] % s[0] == 0 or s[2] % s[1] == 0):
    print('YES')
else:
    print('NO')

