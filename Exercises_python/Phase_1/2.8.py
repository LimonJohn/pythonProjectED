# 2.8 Ход короля
s = []
for i in range(4):
    s.append(int((input())))
if abs(s[0] - s[2]) <= 1 and abs(s[1] - s[3]) <= 1:
    print('YES')
else:
    print('NO')
