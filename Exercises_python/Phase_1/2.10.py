# 2.10 Ход ферзя
s = []
for i in range(4):
    s.append(int((input())))
if s[0] == s[2] or s[1] == s[3]:
    print('YES')
elif abs(s[0] - s[2]) <= 1 and abs(s[1] - s[3]) <= 1:
    print('YES')
elif abs(s[0] - s[2]) == abs(s[1]-s[3]):
    print('YES')
else:
    print('NO')