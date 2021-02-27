# 2.5 Минимум из трех чисел
'''
a = []
for i in range(3):
    a.append(int(input()))
print(min(a))
'''
a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)
