# 2.11 Ход коня
s = []
for i in range(4):
    s.append(int((input())))
if abs(s[0] - s[2]) == 1 and abs(s[1] - s[3]) == 2 or \
        abs(s[0] - s[2]) == 2 and abs(s[1] - s[3]) == 1:
    print('YES')
else:
    print('NO')
