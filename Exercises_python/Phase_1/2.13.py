# 2.13 Яша плавает в бассейне
s = []
for i in range(4):
    s.append(int((input())))
if s[0] > s[1]:
    print(min(s[0] - s[3], s[1] - s[2], s[2], s[3]))
else:
    print(min(s[0] - s[2], s[1] - s[3], s[2], s[3]))
