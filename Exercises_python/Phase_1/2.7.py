# 2.7 Ход ладьи
# n = 7
# m = 7
# a = [[(i + j) % 2 for i in range(n)] for j in range(m)]
# for i in range(n):
#    print(end='\n')
#    for j in range(m):
#        print('[', a[i][j], ']  ', end='')

s = []
for i in range(4):
    s.append((input()))
if s[0] == s[2] or s[1] == s[3]:
    print('YES')
else:
    print('NO')
