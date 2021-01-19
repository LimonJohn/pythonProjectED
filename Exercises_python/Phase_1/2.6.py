# 2.6 Сколько совпадает чисел

# s = input().split()
# for i in range(len(s)):
#     s[i] = int(s[i])
s = []
for i in range(3):
    s.append((input()))
if s[0] == s[1] == s[2]:
    print(3)
elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
    print(2)
else:
    print(0)
