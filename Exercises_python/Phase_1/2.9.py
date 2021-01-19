# 2.9 Ход слона
s = []
for i in range(4):
    s.append(int((input())))
if abs(s[0] - s[2]) == abs(s[1]-s[3]):
    print('YES')
else:
    print('NO')
